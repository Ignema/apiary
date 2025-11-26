"""Orchestrator for coordinating the complete MDE pipeline."""

import subprocess
from pathlib import Path
from dataclasses import dataclass
from typing import List, Optional

from src.parser.dsl_parser import DslParser
from src.transformer.ast_to_model import AstToModelTransformer
from src.validator.model_validator import ModelValidator
from src.generator.code_generator import CodeGenerator


@dataclass
class OrchestrationResult:
    """Result of complete pipeline orchestration."""
    success: bool
    output_dir: Optional[Path]
    errors: List[str]
    stage_failed: Optional[str]


class UvHelper:
    """Helper class for UV package manager operations."""
    
    @staticmethod
    def sync(project_dir: Path) -> subprocess.CompletedProcess:
        """
        Run uv sync in project directory to install dependencies.
        
        Args:
            project_dir: Directory containing pyproject.toml
            
        Returns:
            CompletedProcess with result of uv sync command
            
        Raises:
            subprocess.CalledProcessError: If uv sync fails
        """
        try:
            result = subprocess.run(
                ['uv', 'sync'],
                cwd=project_dir,
                capture_output=True,
                text=True,
                check=True
            )
            return result
        except subprocess.CalledProcessError as e:
            raise RuntimeError(
                f"Failed to run 'uv sync': {e.stderr or e.stdout}"
            ) from e
        except FileNotFoundError:
            raise RuntimeError(
                "UV is not installed. Please install UV: https://docs.astral.sh/uv/getting-started/installation/"
            )
    
    @staticmethod
    def run_uvicorn(project_dir: Path, reload: bool = True) -> None:
        """
        Run uvicorn with uv run to start the application.
        
        Args:
            project_dir: Directory containing the FastAPI application
            reload: Whether to enable auto-reload on file changes
            
        Note:
            This method starts a long-running process and does not return
            until the server is stopped (Ctrl+C).
        """
        try:
            cmd = ['uv', 'run', 'uvicorn', 'main:app']
            if reload:
                cmd.append('--reload')
            
            subprocess.run(
                cmd,
                cwd=project_dir,
                check=True
            )
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Failed to run uvicorn: {e}")
        except FileNotFoundError:
            raise RuntimeError(
                "UV is not installed. Please install UV: https://docs.astral.sh/uv/getting-started/installation/"
            )
        except KeyboardInterrupt:
            print("\nServer stopped.")


class ApiaryOrchestrator:
    """Coordinates the complete MDE pipeline from DSL to running application."""
    
    def __init__(self, template_dir: Path):
        """
        Initialize orchestrator with all pipeline components.
        
        Args:
            template_dir: Directory containing Jinja2 templates for code generation
        """
        self.parser = DslParser()
        self.transformer = AstToModelTransformer()
        self.validator = ModelValidator()
        self.generator = CodeGenerator(template_dir)
    
    def generate_from_file(self, dsl_file: Path, output_dir: Path) -> OrchestrationResult:
        """
        Execute complete pipeline from DSL file to generated application.
        
        This method orchestrates the following stages:
        1. Parse DSL file to AST
        2. Transform AST to Ecore model
        3. Validate model against constraints
        4. Generate FastAPI application code
        
        Args:
            dsl_file: Path to DSL specification file
            output_dir: Directory to write generated application
            
        Returns:
            OrchestrationResult with success status and any errors
        """
        errors = []
        
        # Stage 1: Parse DSL file
        parse_result = self.parser.parse_file(dsl_file)
        if not parse_result.success:
            error_messages = [str(error) for error in parse_result.errors]
            return OrchestrationResult(
                success=False,
                output_dir=None,
                errors=error_messages,
                stage_failed='parsing'
            )
        
        # Stage 2: Transform AST to model
        try:
            model = self.transformer.transform(parse_result.ast)
        except Exception as e:
            return OrchestrationResult(
                success=False,
                output_dir=None,
                errors=[f"Transformation error: {str(e)}"],
                stage_failed='transformation'
            )
        
        # Stage 3: Validate model
        validation_result = self.validator.validate(model)
        if not validation_result.valid:
            error_messages = [
                f"{error.constraint}: {error.message}" + 
                (f" (at {error.location})" if error.location else "")
                for error in validation_result.errors
            ]
            return OrchestrationResult(
                success=False,
                output_dir=None,
                errors=error_messages,
                stage_failed='validation'
            )
        
        # Stage 4: Generate code
        generation_result = self.generator.generate(model, output_dir)
        if not generation_result.success:
            return OrchestrationResult(
                success=False,
                output_dir=output_dir,
                errors=generation_result.errors,
                stage_failed='generation'
            )
        
        # Success!
        return OrchestrationResult(
            success=True,
            output_dir=output_dir,
            errors=[],
            stage_failed=None
        )
    
    def setup_project(self, output_dir: Path) -> bool:
        """
        Initialize generated project by running uv sync.
        
        Args:
            output_dir: Directory containing generated application
            
        Returns:
            True if setup succeeded, False otherwise
        """
        try:
            UvHelper.sync(output_dir)
            return True
        except RuntimeError as e:
            print(f"Error setting up project: {e}")
            return False
    
    def run_application(self, output_dir: Path, reload: bool = True) -> None:
        """
        Run generated application with uvicorn.
        
        Args:
            output_dir: Directory containing generated application
            reload: Whether to enable auto-reload on file changes
            
        Note:
            This method blocks until the server is stopped (Ctrl+C).
        """
        try:
            UvHelper.run_uvicorn(output_dir, reload=reload)
        except RuntimeError as e:
            print(f"Error running application: {e}")
