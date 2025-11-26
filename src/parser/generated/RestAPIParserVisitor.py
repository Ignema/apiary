# Generated from apiary/parser/grammar/RestAPIParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .RestAPIParser import RestAPIParser
else:
    from RestAPIParser import RestAPIParser

# This class defines a complete generic visitor for a parse tree produced by RestAPIParser.

class RestAPIParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RestAPIParser#api_specification.
    def visitApi_specification(self, ctx:RestAPIParser.Api_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RestAPIParser#api_declaration.
    def visitApi_declaration(self, ctx:RestAPIParser.Api_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RestAPIParser#database_type.
    def visitDatabase_type(self, ctx:RestAPIParser.Database_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RestAPIParser#model_declaration.
    def visitModel_declaration(self, ctx:RestAPIParser.Model_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RestAPIParser#field_declaration.
    def visitField_declaration(self, ctx:RestAPIParser.Field_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RestAPIParser#type_spec.
    def visitType_spec(self, ctx:RestAPIParser.Type_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RestAPIParser#field_modifier.
    def visitField_modifier(self, ctx:RestAPIParser.Field_modifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RestAPIParser#value.
    def visitValue(self, ctx:RestAPIParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RestAPIParser#endpoint_declaration.
    def visitEndpoint_declaration(self, ctx:RestAPIParser.Endpoint_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RestAPIParser#http_method.
    def visitHttp_method(self, ctx:RestAPIParser.Http_methodContext):
        return self.visitChildren(ctx)



del RestAPIParser