"""Unit tests for DSL parser."""

import pytest
from src.parser.dsl_parser import DslParser


class TestDslParser:
    """Test DSL parsing functionality."""
    
    def test_parse_simple_api(self):
        """Test parsing a minimal valid API specification."""
        dsl = '''
api "TestAPI" version "1.0.0" at "/api" using sqlite

model User table "users" {
    name: str required
}

endpoint GET "/users" -> User[] description "Get users"
'''
        parser = DslParser()
        result = parser.parse_string(dsl)
        
        assert result.success
        assert result.ast is not None
        assert result.ast.name == "TestAPI"
        assert result.ast.version == "1.0.0"
        assert result.ast.base_url == "/api"
        assert result.ast.database == "sqlite"
        assert len(result.ast.models) == 1
        assert len(result.ast.endpoints) == 1
    
    def test_parse_model_with_fields(self):
        """Test parsing model with various field types."""
        dsl = '''
api "Test" version "1.0.0" at "/api" using sqlite

model Product table "products" {
    name: str required unique
    price: float required
    quantity: int default 0
    active: bool default true
}
'''
        parser = DslParser()
        result = parser.parse_string(dsl)
        
        assert result.success
        model = result.ast.models[0]
        assert model.name == "Product"
        assert model.table_name == "products"
        assert len(model.fields) == 4
        
        # Check field properties
        name_field = model.fields[0]
        assert name_field.name == "name"
        assert name_field.type == "str"
        assert "required" in name_field.modifiers
        assert "unique" in name_field.modifiers
    
    def test_parse_endpoints(self):
        """Test parsing different HTTP methods."""
        dsl = '''
api "Test" version "1.0.0" at "/api" using sqlite

model Item table "items" {
    name: str required
}

endpoint GET "/items" -> Item[] description "List items"
endpoint POST "/items" -> Item description "Create item"
endpoint PUT "/items/{id}" -> Item description "Update item"
endpoint DELETE "/items/{id}" -> bool description "Delete item"
'''
        parser = DslParser()
        result = parser.parse_string(dsl)
        
        assert result.success
        assert len(result.ast.endpoints) == 4
        
        methods = [ep.method for ep in result.ast.endpoints]
        assert "GET" in methods
        assert "POST" in methods
        assert "PUT" in methods
        assert "DELETE" in methods
    
    def test_parse_invalid_syntax(self):
        """Test that invalid syntax produces errors."""
        dsl = '''
api "Test" version "1.0.0" at "/api" using sqlite
model User {
'''
        parser = DslParser()
        result = parser.parse_string(dsl)
        
        assert not result.success
        assert len(result.errors) > 0
