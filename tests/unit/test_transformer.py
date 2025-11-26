"""Unit tests for AST to model transformation."""

import pytest
from src.parser.ast_models import ApiAst, ModelAst, EndpointAst, FieldAst
from src.transformer.ast_to_model import AstToModelTransformer
from src.metamodel.enums import HttpMethod, DatabaseType, FieldType


class TestAstToModelTransformer:
    """Test AST to Ecore model transformation."""
    
    def test_transform_api(self):
        """Test transforming basic API specification."""
        ast = ApiAst(
            name="TestAPI",
            version="1.0.0",
            base_url="/api",
            database="sqlite",
            models=[],
            endpoints=[]
        )
        
        transformer = AstToModelTransformer()
        model = transformer.transform(ast)
        
        assert model.name == "TestAPI"
        assert model.version == "1.0.0"
        assert model.base_url == "/api"
        assert model.database == DatabaseType.SQLITE
    
    def test_transform_model_with_fields(self):
        """Test transforming model with fields."""
        field_ast = FieldAst(
            name="username",
            type="str",
            modifiers=["required", "unique"],
            default=None
        )
        
        model_ast = ModelAst(
            name="User",
            table_name="users",
            fields=[field_ast]
        )
        
        ast = ApiAst(
            name="Test",
            version="1.0.0",
            base_url="/api",
            database="sqlite",
            models=[model_ast],
            endpoints=[]
        )
        
        transformer = AstToModelTransformer()
        model = transformer.transform(ast)
        
        assert len(model.models) == 1
        user_model = model.models[0]
        assert user_model.name == "User"
        assert user_model.table_name == "users"
        assert len(user_model.fields) == 1
        
        field = user_model.fields[0]
        assert field.name == "username"
        assert field.type == FieldType.STR
        assert field.required
        assert field.unique
    
    def test_transform_endpoint(self):
        """Test transforming endpoint with path parameters."""
        endpoint_ast = EndpointAst(
            method="GET",
            path="/users/{id}",
            request_model=None,
            response_model="User",
            description="Get user by ID"
        )
        
        ast = ApiAst(
            name="Test",
            version="1.0.0",
            base_url="/api",
            database="sqlite",
            models=[],
            endpoints=[endpoint_ast]
        )
        
        transformer = AstToModelTransformer()
        model = transformer.transform(ast)
        
        assert len(model.endpoints) == 1
        endpoint = model.endpoints[0]
        assert endpoint.method == HttpMethod.GET
        assert endpoint.path == "/users/{id}"
        assert endpoint.response_model == "User"
        assert endpoint.path_params == ["id"]
