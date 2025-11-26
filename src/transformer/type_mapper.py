"""Type mapping from DSL types to Python/SQLModel types."""

import re
from typing import Tuple
from src.metamodel.enums import FieldType


class TypeMapper:
    """Maps DSL type strings to FieldType enums and handles type modifiers."""
    
    TYPE_MAPPING = {
        'str': FieldType.STR,
        'int': FieldType.INT,
        'float': FieldType.FLOAT,
        'bool': FieldType.BOOL,
        'datetime': FieldType.DATETIME,
    }
    
    @classmethod
    def map_type(cls, dsl_type: str) -> FieldType:
        """
        Map DSL type string to FieldType enum.
        
        Args:
            dsl_type: Type string from DSL (e.g., 'str', 'int', 'Model[]')
        
        Returns:
            FieldType enum value
        
        Raises:
            ValueError: If type is not recognized
        """
        # Handle array notation by stripping [] suffix
        base_type = dsl_type.rstrip('[]')
        
        if base_type not in cls.TYPE_MAPPING:
            raise ValueError(f"Unknown type: {dsl_type}")
        
        return cls.TYPE_MAPPING[base_type]
    
    @classmethod
    def is_array_type(cls, dsl_type: str) -> bool:
        """
        Check if the DSL type represents an array (e.g., 'Model[]').
        
        Args:
            dsl_type: Type string from DSL
        
        Returns:
            True if type ends with '[]', False otherwise
        """
        return dsl_type.endswith('[]')
    
    @classmethod
    def parse_type(cls, dsl_type: str) -> Tuple[FieldType, bool]:
        """
        Parse DSL type string into FieldType and array flag.
        
        Args:
            dsl_type: Type string from DSL
        
        Returns:
            Tuple of (FieldType, is_array)
        """
        is_array = cls.is_array_type(dsl_type)
        field_type = cls.map_type(dsl_type)
        return field_type, is_array
