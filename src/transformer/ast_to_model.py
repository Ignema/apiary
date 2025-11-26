"""Transform AST to Ecore metamodel instances."""

import re
from typing import List
from src.parser.ast_models import ApiAst, ModelAst, EndpointAst, FieldAst
from src.metamodel.models import (
    ApiModel,
    ModelDefinition,
    EndpointDefinition,
    FieldDefinition,
)
from src.metamodel.enums import HttpMethod, DatabaseType
from src.transformer.type_mapper import TypeMapper


class AstToModelTransformer:
    """Transforms Abstract Syntax Tree to Ecore metamodel instances."""
    
    def __init__(self):
        self.type_mapper = TypeMapper()
    
    def transform(self, ast: ApiAst) -> ApiModel:
        """
        Transform ApiAst to ApiModel.
        
        Args:
            ast: Abstract Syntax Tree from parser
        
        Returns:
            ApiModel instance with all components transformed
        """
        # Transform database type
        database = self._transform_database_type(ast.database)
        
        # Transform models
        models = [self._transform_model(model_ast) for model_ast in ast.models]
        
        # Transform endpoints
        endpoints = [self._transform_endpoint(endpoint_ast) for endpoint_ast in ast.endpoints]
        
        return ApiModel(
            name=ast.name,
            version=ast.version,
            base_url=ast.base_url,
            database=database,
            models=models,
            endpoints=endpoints,
        )
    
    def _transform_database_type(self, database: str) -> DatabaseType:
        """
        Transform database string to DatabaseType enum.
        
        Args:
            database: Database type string from AST
        
        Returns:
            DatabaseType enum value
        
        Raises:
            ValueError: If database type is not recognized
        """
        try:
            return DatabaseType(database.lower())
        except ValueError:
            raise ValueError(f"Unknown database type: {database}")
    
    def _transform_model(self, model_ast: ModelAst) -> ModelDefinition:
        """
        Transform ModelAst to ModelDefinition.
        
        Args:
            model_ast: Model AST node
        
        Returns:
            ModelDefinition instance
        """
        fields = [self._transform_field(field_ast) for field_ast in model_ast.fields]
        
        return ModelDefinition(
            name=model_ast.name,
            table_name=model_ast.table_name,
            fields=fields,
        )
    
    def _transform_endpoint(self, endpoint_ast: EndpointAst) -> EndpointDefinition:
        """
        Transform EndpointAst to EndpointDefinition.
        
        Args:
            endpoint_ast: Endpoint AST node
        
        Returns:
            EndpointDefinition instance
        """
        # Transform HTTP method
        method = HttpMethod(endpoint_ast.method.upper())
        
        # Extract path parameters
        path_params = self._extract_path_parameters(endpoint_ast.path)
        
        return EndpointDefinition(
            path=endpoint_ast.path,
            method=method,
            request_model=endpoint_ast.request_model,
            response_model=endpoint_ast.response_model,
            description=endpoint_ast.description,
            path_params=path_params,
        )
    
    def _transform_field(self, field_ast: FieldAst) -> FieldDefinition:
        """
        Transform FieldAst to FieldDefinition.
        
        Args:
            field_ast: Field AST node
        
        Returns:
            FieldDefinition instance
        """
        # Map type
        field_type = self.type_mapper.map_type(field_ast.type)
        
        # Extract modifiers
        required = 'required' in field_ast.modifiers
        unique = 'unique' in field_ast.modifiers
        indexed = 'indexed' in field_ast.modifiers
        
        # Parse default value
        default = self._parse_default_value(field_ast.default) if field_ast.default else None
        
        return FieldDefinition(
            name=field_ast.name,
            type=field_type,
            required=required,
            unique=unique,
            indexed=indexed,
            default=default,
        )
    
    def _extract_path_parameters(self, path: str) -> List[str]:
        """
        Extract path parameters from endpoint path.
        
        Args:
            path: Endpoint path (e.g., '/tasks/{id}/comments/{comment_id}')
        
        Returns:
            List of parameter names (e.g., ['id', 'comment_id'])
        """
        return re.findall(r'\{(\w+)\}', path)
    
    def _parse_default_value(self, default_str: str) -> any:
        """
        Parse default value string to appropriate Python type.
        
        Args:
            default_str: Default value as string from AST
        
        Returns:
            Parsed default value
        """
        # Remove quotes from string literals
        if default_str.startswith('"') and default_str.endswith('"'):
            return default_str[1:-1]
        if default_str.startswith("'") and default_str.endswith("'"):
            return default_str[1:-1]
        
        # Parse boolean
        if default_str.lower() == 'true':
            return True
        if default_str.lower() == 'false':
            return False
        
        # Try to parse as number
        try:
            if '.' in default_str:
                return float(default_str)
            return int(default_str)
        except ValueError:
            pass
        
        # Return as string if nothing else matches
        return default_str
