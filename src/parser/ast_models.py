"""Abstract Syntax Tree data models."""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class FieldAst:
    """AST node for field declaration."""
    name: str
    type: str
    modifiers: List[str] = field(default_factory=list)
    default: Optional[str] = None


@dataclass
class ModelAst:
    """AST node for model declaration."""
    name: str
    table_name: str
    fields: List[FieldAst] = field(default_factory=list)


@dataclass
class EndpointAst:
    """AST node for endpoint declaration."""
    method: str
    path: str
    request_model: Optional[str]
    response_model: str
    description: str = ""


@dataclass
class ApiAst:
    """Root AST node for API specification."""
    name: str
    version: str
    base_url: str
    database: str
    models: List[ModelAst] = field(default_factory=list)
    endpoints: List[EndpointAst] = field(default_factory=list)
