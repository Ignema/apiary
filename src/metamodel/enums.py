"""Enum definitions for the metamodel."""

from enum import Enum


class HttpMethod(Enum):
    """HTTP methods supported by the DSL."""
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"


class FieldType(Enum):
    """Field types supported by the DSL."""
    STR = "str"
    INT = "int"
    FLOAT = "float"
    BOOL = "bool"
    DATETIME = "datetime"


class DatabaseType(Enum):
    """Database types supported by the DSL."""
    SQLITE = "sqlite"
    POSTGRES = "postgres"
