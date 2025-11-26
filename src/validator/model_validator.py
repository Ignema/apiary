"""Model validator with OCL-inspired constraint checking."""

import re
from dataclasses import dataclass, field
from typing import List, Optional
from src.metamodel.models import ApiModel, EndpointDefinition
from src.metamodel.enums import HttpMethod


@dataclass
class ValidationError:
    """Represents a validation constraint violation."""
    constraint: str
    message: str
    location: Optional[str] = None


@dataclass
class ValidationResult:
    """Result of model validation."""
    valid: bool
    errors: List[ValidationError] = field(default_factory=list)


class ModelValidator:
    """Validates API models against semantic constraints."""
    
    def validate(self, model: ApiModel) -> ValidationResult:
        """
        Validate model against all constraints.
        
        Args:
            model: The API model to validate
            
        Returns:
            ValidationResult with success status and any errors
        """
        errors: List[ValidationError] = []
        
        # Run all constraint checks
        errors.extend(self._check_unique_endpoints(model))
        errors.extend(self._check_model_names(model))
        errors.extend(self._check_table_names(model))
        errors.extend(self._check_request_models(model))
        errors.extend(self._check_path_parameters(model))
        errors.extend(self._check_version_format(model))
        
        return ValidationResult(
            valid=len(errors) == 0,
            errors=errors
        )
    
    def _check_unique_endpoints(self, model: ApiModel) -> List[ValidationError]:
        """
        Ensure endpoint (path, method) tuples are unique.
        
        Requirement 2.1: Endpoint uniqueness constraint
        """
        errors = []
        seen = set()
        
        for endpoint in model.endpoints:
            key = (endpoint.path, endpoint.method)
            if key in seen:
                errors.append(ValidationError(
                    constraint="endpoint_uniqueness",
                    message=f"Duplicate endpoint: {endpoint.method.value} {endpoint.path}",
                    location=f"{endpoint.method.value} {endpoint.path}"
                ))
            seen.add(key)
        
        return errors
    
    def _check_model_names(self, model: ApiModel) -> List[ValidationError]:
        """
        Verify model names start with uppercase and follow pattern.
        
        Requirement 2.2: Model naming constraint
        Pattern: ^[A-Z][a-zA-Z0-9]*$
        """
        errors = []
        pattern = re.compile(r'^[A-Z][a-zA-Z0-9]*$')
        
        for model_def in model.models:
            if not pattern.match(model_def.name):
                errors.append(ValidationError(
                    constraint="model_naming",
                    message=f"Model name '{model_def.name}' must start with uppercase letter and contain only alphanumeric characters",
                    location=f"model {model_def.name}"
                ))
        
        return errors
    
    def _check_table_names(self, model: ApiModel) -> List[ValidationError]:
        """
        Verify table names are lowercase with underscores only.
        
        Requirement 2.3: Table naming constraint
        Pattern: ^[a-z][a-z0-9_]*$
        """
        errors = []
        pattern = re.compile(r'^[a-z][a-z0-9_]*$')
        
        for model_def in model.models:
            if not pattern.match(model_def.table_name):
                errors.append(ValidationError(
                    constraint="table_naming",
                    message=f"Table name '{model_def.table_name}' must be lowercase and contain only letters, numbers, and underscores",
                    location=f"model {model_def.name}"
                ))
        
        return errors
    
    def _check_request_models(self, model: ApiModel) -> List[ValidationError]:
        """
        Verify POST, PUT, PATCH endpoints have request models.
        
        Requirement 2.4: Request model constraint for mutating endpoints
        """
        errors = []
        mutating_methods = {HttpMethod.POST, HttpMethod.PUT, HttpMethod.PATCH}
        
        for endpoint in model.endpoints:
            if endpoint.method in mutating_methods and not endpoint.request_model:
                errors.append(ValidationError(
                    constraint="request_model_required",
                    message=f"{endpoint.method.value} endpoint must specify a request model",
                    location=f"{endpoint.method.value} {endpoint.path}"
                ))
        
        return errors
    
    def _check_path_parameters(self, model: ApiModel) -> List[ValidationError]:
        """
        Verify path parameters exist in endpoint definition.
        
        Requirement 2.5: Path parameter validation
        """
        errors = []
        
        for endpoint in model.endpoints:
            # Extract parameters from path using regex
            path_params_in_path = set(re.findall(r'\{(\w+)\}', endpoint.path))
            defined_params = set(endpoint.path_params)
            
            # Check for parameters in path that aren't defined
            missing_params = path_params_in_path - defined_params
            if missing_params:
                errors.append(ValidationError(
                    constraint="path_parameter_validation",
                    message=f"Path parameters {missing_params} are not defined in endpoint",
                    location=f"{endpoint.method.value} {endpoint.path}"
                ))
        
        return errors
    
    def _check_version_format(self, model: ApiModel) -> List[ValidationError]:
        """
        Verify version follows semantic versioning format.
        
        Requirement 2.6: Version format validation
        Pattern: ^\\d+\\.\\d+\\.\\d+$
        """
        errors = []
        pattern = re.compile(r'^\d+\.\d+\.\d+$')
        
        if not pattern.match(model.version):
            errors.append(ValidationError(
                constraint="version_format",
                message=f"Version '{model.version}' must follow semantic versioning format (e.g., 1.0.0)",
                location="api version"
            ))
        
        return errors
