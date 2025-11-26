# Contributing to Apiary

Thank you for your interest in contributing to Apiary! This document provides guidelines for contributing to the project.

## Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ignema/apiary.git
   cd apiary
   ```

2. **Install UV** (if not already installed)
   ```bash
   # See https://docs.astral.sh/uv/getting-started/installation/
   ```

3. **Install dependencies**
   ```bash
   uv sync --extra dev
   ```

4. **Run tests**
   ```bash
   uv run pytest tests/ -v
   ```

## Development Workflow

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Write clear, concise code
   - Follow existing code style
   - Add tests for new functionality
   - Update documentation as needed

3. **Run tests**
   ```bash
   uv run pytest tests/ -v
   uv run pytest --cov=src tests/
   ```

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```

   Use conventional commit messages:
   - `feat:` for new features
   - `fix:` for bug fixes
   - `docs:` for documentation changes
   - `test:` for test additions/changes
   - `refactor:` for code refactoring
   - `chore:` for maintenance tasks

5. **Push and create a pull request**
   ```bash
   git push origin feature/your-feature-name
   ```

## Code Style

- Follow PEP 8 guidelines
- Use type hints where appropriate
- Write docstrings for public functions and classes
- Keep functions focused and concise

## Testing

- Write unit tests for individual components
- Write integration tests for end-to-end workflows
- Aim for high test coverage
- Tests should be fast and deterministic

## Reporting Issues

When reporting issues, please include:
- A clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Your environment (OS, Python version, UV version)
- Relevant error messages or logs

## Questions?

Feel free to open an issue for questions or discussions about the project.
