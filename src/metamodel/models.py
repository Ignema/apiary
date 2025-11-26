"""Metamodel data models inspired by Ecore."""

from dataclasses import dataclass, field
from typing import List, Optional, Any
from src.metamodel.enums import HttpMethod, FieldType, DatabaseType


@dataclass
class FieldDefinition:
    """Represents a model field with constraints."""
    name: str
    type: FieldType
    required: bool = False
    unique: bool = False
    indexed: bool = False
    default: Optional[Any] = None


@dataclass
class ModelDefinition:
    """Represents a data model with fields."""
    name: str
    table_name: str
    fields: List[FieldDefinition] = field(default_factory=list)


@dataclass
class EndpointDefinition:
    """Represents an HTTP endpoint."""
    path: str
    method: HttpMethod
    request_model: Optional[str]
    response_model: str
    description: str = ""
    path_params: List[str] = field(default_factory=list)


@dataclass
class ApiModel:
    """Represents a complete API specification."""
    name: str
    version: str
    base_url: str
    database: DatabaseType
    models: List[ModelDefinition] = field(default_factory=list)
    endpoints: List[EndpointDefinition] = field(default_factory=list)
