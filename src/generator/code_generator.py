"""Code generator for FastAPI applications using Jinja2 templates."""

import re
from pathlib import Path
from typing import List
from dataclasses import dataclass
from jinja2 import Environment, FileSystemLoader, TemplateError

from src.metamodel.models import ApiModel


@dataclass
class GenerationResult:
    """Result of code generation process."""
    success: bool
    output_dir: Path
    files_created: List[Path]
    errors: List[str]


class CodeGenerator:
    """Generates FastAPI application code from validated API models."""
    
    def __init__(self, template_dir: Path):
        """
        Initialize code generator with Jinja2 environment.
        
        Args:
            template_dir: Directory containing Jinja2 templates
        """
        self.template_dir = template_dir
        self.env = Environment(
            loader=FileSystemLoader(str(template_dir)),
            trim_blocks=False,
            lstrip_blocks=False
        )
        
        # Register custom filters
        self.env.filters['snake_case'] = self._to_snake_case
        self.env.filters['kebab_case'] = self._to_kebab_case
        self.env.filters['plural'] = self._to_plural
    
    @staticmethod
    def _to_snake_case(text: str) -> str:
        """
        Convert PascalCase or camelCase to snake_case.
        
        Examples:
            PetStore -> pet_store
            petStore -> pet_store
            APIKey -> api_key
        
        Args:
            text: Input text in PascalCase or camelCase
            
        Returns:
            Text converted to snake_case
        """
        # Insert underscore before uppercase letters
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
        # Insert underscore before uppercase letters followed by lowercase
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
    
    @staticmethod
    def _to_kebab_case(text: str) -> str:
        """
        Convert PascalCase or camelCase to kebab-case.
        
        Examples:
            PetStore -> pet-store
            petStore -> pet-store
            APIKey -> api-key
        
        Args:
            text: Input text in PascalCase or camelCase
            
        Returns:
            Text converted to kebab-case
        """
        # Insert hyphen before uppercase letters
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1-\2', text)
        # Insert hyphen before uppercase letters followed by lowercase
        return re.sub('([a-z0-9])([A-Z])', r'\1-\2', s1).lower()
    
    @staticmethod
    def _to_plural(text: str) -> str:
        """
        Simple pluralization for common cases.
        
        Examples:
            Task -> tasks
            Pet -> pets
            Category -> categories
        
        Args:
            text: Singular noun
            
        Returns:
            Pluralized form
        """
        text_lower = text.lower()
        
        # Handle special cases
        if text_lower.endswith('y') and len(text_lower) > 1 and text_lower[-2] not in 'aeiou':
            # category -> categories
            return text_lower[:-1] + 'ies'
        elif text_lower.endswith(('s', 'x', 'z', 'ch', 'sh')):
            # class -> classes, box -> boxes
            return text_lower + 'es'
        else:
            # Default: just add 's'
            return text_lower + 's'
    
    def generate(self, model: ApiModel, output_dir: Path) -> GenerationResult:
        """
        Generate complete FastAPI application from API model.
        
        Args:
            model: Validated API model to generate code from
            output_dir: Directory to write generated files
            
        Returns:
            GenerationResult with success status and files created
        """
        files_created = []
        errors = []
        
        try:
            # Create output directory if it doesn't exist
            output_dir.mkdir(parents=True, exist_ok=True)
            
            # Generate all application files
            generation_methods = [
                ('main.py', self._generate_main),
                ('models.py', self._generate_models),
                ('database.py', self._generate_database),
                ('pyproject.toml', self._generate_pyproject),
                ('README.md', self._generate_readme),
            ]
            
            for filename, method in generation_methods:
                try:
                    content = method(model)
                    file_path = output_dir / filename
                    file_path.write_text(content, encoding='utf-8')
                    files_created.append(file_path)
                except TemplateError as e:
                    errors.append(f"Template error in {filename}: {str(e)}")
                except Exception as e:
                    errors.append(f"Error generating {filename}: {str(e)}")
            
            # Create .python-version file
            try:
                python_version_file = output_dir / '.python-version'
                python_version_file.write_text('3.11\n', encoding='utf-8')
                files_created.append(python_version_file)
            except Exception as e:
                errors.append(f"Error creating .python-version: {str(e)}")
            
            success = len(errors) == 0
            
            return GenerationResult(
                success=success,
                output_dir=output_dir,
                files_created=files_created,
                errors=errors
            )
            
        except Exception as e:
            return GenerationResult(
                success=False,
                output_dir=output_dir,
                files_created=files_created,
                errors=[f"Fatal error during generation: {str(e)}"]
            )
    
    def _generate_main(self, model: ApiModel) -> str:
        """
        Generate main.py with FastAPI app and route handlers.
        
        Args:
            model: API model
            
        Returns:
            Generated main.py content
        """
        template = self.env.get_template('main.jinja')
        return template.render(model=model)
    
    def _generate_models(self, model: ApiModel) -> str:
        """
        Generate models.py with SQLModel class definitions.
        
        Args:
            model: API model
            
        Returns:
            Generated models.py content
        """
        template = self.env.get_template('models.jinja')
        return template.render(model=model)
    
    def _generate_database(self, model: ApiModel) -> str:
        """
        Generate database.py with engine and session management.
        
        Args:
            model: API model
            
        Returns:
            Generated database.py content
        """
        template = self.env.get_template('database.jinja')
        return template.render(model=model)
    
    def _generate_pyproject(self, model: ApiModel) -> str:
        """
        Generate pyproject.toml with UV-compatible configuration.
        
        Args:
            model: API model
            
        Returns:
            Generated pyproject.toml content
        """
        template = self.env.get_template('pyproject.jinja')
        return template.render(model=model)
    
    def _generate_readme(self, model: ApiModel) -> str:
        """
        Generate README.md with setup and usage instructions.
        
        Args:
            model: API model
            
        Returns:
            Generated README.md content
        """
        template = self.env.get_template('readme.jinja')
        return template.render(model=model)
