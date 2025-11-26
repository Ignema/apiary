"""Integration tests for complete MDE pipeline."""

import pytest
from pathlib import Path
import tempfile
import shutil
from src.orchestrator import ApiaryOrchestrator


class TestPipeline:
    """Test complete pipeline from DSL to generated code."""
    
    def test_end_to_end_generation(self):
        """Test complete pipeline with valid DSL."""
        dsl_content = '''
api "PetStore" version "1.0.0" at "/api/v1" using sqlite

model Pet table "pets" {
    name: str required
    age: int default 0
}

endpoint GET "/pets" -> Pet[] description "Get all pets"
endpoint POST "/pets" -> Pet description "Create a pet"
'''
        
        # Create temporary directories
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            dsl_file = temp_path / "test.api"
            output_dir = temp_path / "output"
            template_dir = Path("templates")
            
            # Write DSL file
            dsl_file.write_text(dsl_content)
            
            # Run orchestrator
            orchestrator = ApiaryOrchestrator(template_dir)
            result = orchestrator.generate_from_file(dsl_file, output_dir)
            
            # Verify success
            assert result.success
            assert result.stage_failed is None
            assert len(result.errors) == 0
            
            # Verify generated files exist
            assert (output_dir / "main.py").exists()
            assert (output_dir / "models.py").exists()
            assert (output_dir / "database.py").exists()
            assert (output_dir / "pyproject.toml").exists()
    
    def test_pipeline_with_invalid_dsl(self):
        """Test pipeline fails gracefully with invalid DSL."""
        dsl_content = '''
api "Test" version "1.0" at "/api" using sqlite
'''
        
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            dsl_file = temp_path / "test.api"
            output_dir = temp_path / "output"
            template_dir = Path("templates")
            
            dsl_file.write_text(dsl_content)
            
            orchestrator = ApiaryOrchestrator(template_dir)
            result = orchestrator.generate_from_file(dsl_file, output_dir)
            
            # Should fail validation due to invalid version format
            assert not result.success
            assert result.stage_failed == "validation"
            assert len(result.errors) > 0
