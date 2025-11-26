"""DSL parser wrapper for ANTLR-generated parser."""

from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from antlr4.error.ErrorListener import ErrorListener

from src.parser.generated.RestAPILexer import RestAPILexer
from src.parser.generated.RestAPIParser import RestAPIParser
from src.parser.generated.RestAPIParserVisitor import RestAPIParserVisitor
from src.parser.ast_models import (
    ApiAst, ModelAst, EndpointAst, FieldAst
)


@dataclass
class ParseError:
    """Represents a parse error with location information."""
    line: int
    column: int
    message: str

    def __str__(self) -> str:
        return f"Line {self.line}:{self.column} - {self.message}"


@dataclass
class ParseResult:
    """Result of parsing operation."""
    ast: Optional[ApiAst]
    errors: List[ParseError]
    success: bool


class ApiaryErrorListener(ErrorListener):
    """Custom error listener to collect parse errors."""

    def __init__(self):
        super().__init__()
        self.errors: List[ParseError] = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        """Called when a syntax error is encountered."""
        self.errors.append(ParseError(line=line, column=column, message=msg))


class ASTBuilder(RestAPIParserVisitor):
    """Visitor that builds AST from ANTLR parse tree."""

    def visitApi_specification(self, ctx: RestAPIParser.Api_specificationContext) -> ApiAst:
        """Visit the root api_specification node."""
        api_decl = self.visit(ctx.api_declaration())
        
        models = []
        for model_ctx in ctx.model_declaration():
            models.append(self.visit(model_ctx))
        
        endpoints = []
        for endpoint_ctx in ctx.endpoint_declaration():
            endpoints.append(self.visit(endpoint_ctx))
        
        return ApiAst(
            name=api_decl['name'],
            version=api_decl['version'],
            base_url=api_decl['base_url'],
            database=api_decl['database'],
            models=models,
            endpoints=endpoints
        )

    def visitApi_declaration(self, ctx: RestAPIParser.Api_declarationContext) -> dict:
        """Visit api_declaration node."""
        # api STRING version STRING at STRING using database_type
        name = self._unquote(ctx.STRING(0).getText())
        version = self._unquote(ctx.STRING(1).getText())
        base_url = self._unquote(ctx.STRING(2).getText())
        database = self.visit(ctx.database_type())
        
        return {
            'name': name,
            'version': version,
            'base_url': base_url,
            'database': database
        }

    def visitDatabase_type(self, ctx: RestAPIParser.Database_typeContext) -> str:
        """Visit database_type node."""
        if ctx.SQLITE():
            return 'sqlite'
        elif ctx.POSTGRES():
            return 'postgres'
        return 'sqlite'

    def visitModel_declaration(self, ctx: RestAPIParser.Model_declarationContext) -> ModelAst:
        """Visit model_declaration node."""
        # model IDENTIFIER table STRING { field_declaration* }
        name = ctx.IDENTIFIER().getText()
        table_name = self._unquote(ctx.STRING().getText())
        
        fields = []
        for field_ctx in ctx.field_declaration():
            fields.append(self.visit(field_ctx))
        
        return ModelAst(name=name, table_name=table_name, fields=fields)

    def visitField_declaration(self, ctx: RestAPIParser.Field_declarationContext) -> FieldAst:
        """Visit field_declaration node."""
        # IDENTIFIER : type_spec field_modifier* (default value)?
        name = ctx.IDENTIFIER().getText()
        field_type = self.visit(ctx.type_spec())
        
        modifiers = []
        for modifier_ctx in ctx.field_modifier():
            modifiers.append(self.visit(modifier_ctx))
        
        default = None
        if ctx.value():
            default = self.visit(ctx.value())
        
        return FieldAst(
            name=name,
            type=field_type,
            modifiers=modifiers,
            default=default
        )

    def visitType_spec(self, ctx: RestAPIParser.Type_specContext) -> str:
        """Visit type_spec node."""
        if ctx.STR():
            return 'str'
        elif ctx.INT():
            return 'int'
        elif ctx.FLOAT():
            return 'float'
        elif ctx.BOOL():
            return 'bool'
        elif ctx.DATETIME():
            return 'datetime'
        elif ctx.IDENTIFIER():
            # Check if it's an array type
            if ctx.LBRACKET() and ctx.RBRACKET():
                return f"{ctx.IDENTIFIER().getText()}[]"
            else:
                return ctx.IDENTIFIER().getText()
        return 'str'

    def visitField_modifier(self, ctx: RestAPIParser.Field_modifierContext) -> str:
        """Visit field_modifier node."""
        if ctx.REQUIRED():
            return 'required'
        elif ctx.UNIQUE():
            return 'unique'
        elif ctx.INDEXED():
            return 'indexed'
        return ''

    def visitValue(self, ctx: RestAPIParser.ValueContext) -> str:
        """Visit value node."""
        if ctx.STRING():
            return self._unquote(ctx.STRING().getText())
        elif ctx.NUMBER():
            return ctx.NUMBER().getText()
        elif ctx.BOOLEAN():
            return ctx.BOOLEAN().getText()
        elif ctx.NULL():
            return 'null'
        return ''

    def visitEndpoint_declaration(self, ctx: RestAPIParser.Endpoint_declarationContext) -> EndpointAst:
        """Visit endpoint_declaration node."""
        # endpoint http_method STRING -> type_spec (description STRING)?
        method = self.visit(ctx.http_method())
        path = self._unquote(ctx.STRING(0).getText())
        response_model = self.visit(ctx.type_spec())
        
        description = ''
        if ctx.DESCRIPTION():
            description = self._unquote(ctx.STRING(1).getText())
        
        # Determine request_model based on method
        # For POST, PUT, PATCH, we expect the response_model to be the request model
        # This is a simplification; real DSL might have explicit request model syntax
        request_model = None
        if method in ['POST', 'PUT', 'PATCH']:
            request_model = response_model
        
        return EndpointAst(
            method=method,
            path=path,
            request_model=request_model,
            response_model=response_model,
            description=description
        )

    def visitHttp_method(self, ctx: RestAPIParser.Http_methodContext) -> str:
        """Visit http_method node."""
        if ctx.GET():
            return 'GET'
        elif ctx.POST():
            return 'POST'
        elif ctx.PUT():
            return 'PUT'
        elif ctx.PATCH():
            return 'PATCH'
        elif ctx.DELETE():
            return 'DELETE'
        return 'GET'

    @staticmethod
    def _unquote(text: str) -> str:
        """Remove quotes from string literals."""
        if text.startswith('"') and text.endswith('"'):
            return text[1:-1]
        return text


class DslParser:
    """Main DSL parser wrapper."""

    def parse_file(self, file_path: Path) -> ParseResult:
        """Parse DSL file and return AST or errors."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            return self.parse_string(content)
        except FileNotFoundError:
            return ParseResult(
                ast=None,
                errors=[ParseError(line=0, column=0, message=f"File not found: {file_path}")],
                success=False
            )
        except Exception as e:
            return ParseResult(
                ast=None,
                errors=[ParseError(line=0, column=0, message=f"Error reading file: {str(e)}")],
                success=False
            )

    def parse_string(self, content: str) -> ParseResult:
        """Parse DSL string and return AST or errors."""
        # Create input stream
        input_stream = InputStream(content)
        
        # Create lexer
        lexer = RestAPILexer(input_stream)
        error_listener = ApiaryErrorListener()
        lexer.removeErrorListeners()
        lexer.addErrorListener(error_listener)
        
        # Create token stream
        token_stream = CommonTokenStream(lexer)
        
        # Create parser
        parser = RestAPIParser(token_stream)
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)
        
        # Parse
        try:
            tree = parser.api_specification()
            
            # Check for errors
            if error_listener.errors:
                return ParseResult(
                    ast=None,
                    errors=error_listener.errors,
                    success=False
                )
            
            # Build AST
            builder = ASTBuilder()
            ast = builder.visit(tree)
            
            return ParseResult(
                ast=ast,
                errors=[],
                success=True
            )
        except Exception as e:
            return ParseResult(
                ast=None,
                errors=[ParseError(line=0, column=0, message=f"Parse error: {str(e)}")],
                success=False
            )
