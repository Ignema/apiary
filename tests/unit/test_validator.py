"""Unit tests for model validation."""

import pytest
from src.metamodel.models import ApiModel, ModelDefinition, EndpointDefinition, FieldDefinition
from src.metamodel.enums import HttpMethod, DatabaseType, FieldType
from src.validator.model_validator import ModelValidator


class TestModelValidator:
    """Test model validation constraints."""
    
    def test_valid_model(self):
        """Test that a valid model passes validation."""
        model = ApiModel(
            name="TestAPI",
            version="1.0.0",
            base_url="/api",
            database=DatabaseType.SQLITE,
            models=[
                ModelDefinition(
                    name="User",
                    table_name="users",
                    fields=[
                        FieldDefinition(name="name", type=FieldType.STR, required=True)
                    ]
                )
            ],
            endpoints=[
                EndpointDefinition(
                    path="/users",
                    method=HttpMethod.GET,
                    request_model=None,
                    response_model="User[]",
                    path_params=[]
                )
            ]
        )
        
        validator = ModelValidator()
        result = validator.validate(model)
        
        assert result.valid
        assert len(result.errors) == 0
    
    def test_duplicate_endpoints(self):
        """Test that duplicate endpoints are detected."""
        model = ApiModel(
            name="TestAPI",
            version="1.0.0",
            base_url="/api",
            database=DatabaseType.SQLITE,
            models=[],
            endpoints=[
                EndpointDefinition(
                    path="/users",
                    method=HttpMethod.GET,
                    request_model=None,
                    response_model="User[]",
                    path_params=[]
                ),
                EndpointDefinition(
                    path="/users",
                    method=HttpMethod.GET,
                    request_model=None,
                    response_model="User[]",
                    path_params=[]
                )
            ]
        )
        
        validator = ModelValidator()
        result = validator.validate(model)
        
        assert not result.valid
        assert any("Duplicate endpoint" in err.message for err in result.errors)
    
    def test_invalid_model_name(self):
        """Test that invalid model names are detected."""
        model = ApiModel(
            name="TestAPI",
            version="1.0.0",
            base_url="/api",
            database=DatabaseType.SQLITE,
            models=[
                ModelDefinition(
                    name="user",  # Should start with uppercase
                    table_name="users",
                    fields=[]
                )
            ],
            endpoints=[]
        )
        
        validator = ModelValidator()
        result = validator.validate(model)
        
        assert not result.valid
        assert any("must start with uppercase" in err.message for err in result.errors)
    
    def test_invalid_table_name(self):
        """Test that invalid table names are detected."""
        model = ApiModel(
            name="TestAPI",
            version="1.0.0",
            base_url="/api",
            database=DatabaseType.SQLITE,
            models=[
                ModelDefinition(
                    name="User",
                    table_name="Users",  # Should be lowercase
                    fields=[]
                )
            ],
            endpoints=[]
        )
        
        validator = ModelValidator()
        result = validator.validate(model)
        
        assert not result.valid
        assert any("must be lowercase" in err.message for err in result.errors)
    
    def test_missing_request_model(self):
        """Test that POST endpoints require request models."""
        model = ApiModel(
            name="TestAPI",
            version="1.0.0",
            base_url="/api",
            database=DatabaseType.SQLITE,
            models=[],
            endpoints=[
                EndpointDefinition(
                    path="/users",
                    method=HttpMethod.POST,
                    request_model=None,  # Missing request model
                    response_model="User",
                    path_params=[]
                )
            ]
        )
        
        validator = ModelValidator()
        result = validator.validate(model)
        
        assert not result.valid
        assert any("must specify a request model" in err.message for err in result.errors)
    
    def test_invalid_version_format(self):
        """Test that invalid version format is detected."""
        model = ApiModel(
            name="TestAPI",
            version="1.0",  # Should be semantic versioning (1.0.0)
            base_url="/api",
            database=DatabaseType.SQLITE,
            models=[],
            endpoints=[]
        )
        
        validator = ModelValidator()
        result = validator.validate(model)
        
        assert not result.valid
        assert any("semantic versioning" in err.message for err in result.errors)
