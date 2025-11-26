"""Command-line interface for Apiary."""

import click
from pathlib import Path
import sys

from src.orchestrator import ApiaryOrchestrator


@click.command()
@click.argument('dsl_file', type=click.Path(exists=True, path_type=Path))
@click.argument('output_dir', type=click.Path(path_type=Path))
@click.option('--run', is_flag=True, help='Run generated application after creation')
def generate(dsl_file: Path, output_dir: Path, run: bool):
    """
    Generate FastAPI application from DSL file.
    
    DSL_FILE: Path to the .api DSL specification file
    
    OUTPUT_DIR: Directory where the generated application will be created
    """
    # Get template directory (relative to this file)
    template_dir = Path(__file__).parent.parent / 'templates'
    
    if not template_dir.exists():
        click.echo(click.style('✗ Error: Templates directory not found', fg='red'), err=True)
        sys.exit(1)
    
    # Create orchestrator and run pipeline
    click.echo(f'Generating FastAPI application from {dsl_file}...')
    orchestrator = ApiaryOrchestrator(template_dir)
    
    result = orchestrator.generate_from_file(dsl_file, output_dir)
    
    if result.success:
        click.echo(click.style(f'✓ Generated application in {output_dir}', fg='green'))
        
        # Setup project with UV
        click.echo('\nInstalling dependencies with UV...')
        if orchestrator.setup_project(output_dir):
            click.echo(click.style('✓ Dependencies installed successfully', fg='green'))
            
            # Run application if requested
            if run:
                click.echo('\nStarting application...')
                click.echo(f'API documentation will be available at: http://localhost:8000/docs')
                orchestrator.run_application(output_dir)
            else:
                click.echo('\nTo run the application:')
                click.echo(f'  cd {output_dir}')
                click.echo('  uv run uvicorn main:app --reload')
        else:
            click.echo(click.style('✗ Failed to install dependencies', fg='red'), err=True)
            sys.exit(1)
    else:
        click.echo(click.style(f'✗ Generation failed at {result.stage_failed} stage', fg='red'), err=True)
        click.echo('\nErrors:', err=True)
        for error in result.errors:
            click.echo(f'  • {error}', err=True)
        sys.exit(1)


def main():
    """Entry point for CLI."""
    generate()


if __name__ == '__main__':
    main()
