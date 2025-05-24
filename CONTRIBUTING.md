# Contributing to DNA Sequence Analysis Tool

Thank you for your interest in contributing to the DNA Sequence Analysis Tool! We welcome contributions from the community to help improve this project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Code Style](#code-style)
- [Testing](#testing)
- [Documentation](#documentation)
- [Submitting a Pull Request](#submitting-a-pull-request)
- [Reporting Issues](#reporting-issues)
- [Feature Requests](#feature-requests)

## Code of Conduct

This project adheres to the Contributor Covenant [code of conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally
3. Set up the development environment (see below)
4. Create a new branch for your changes
5. Make your changes
6. Run tests
7. Submit a pull request

## Development Setup

### Prerequisites

- Python 3.8+
- [Poetry](https://python-poetry.org/) for dependency management
- [pre-commit](https://pre-commit.com/) for git hooks

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/DNASequenceAnalysisTool.git
   cd DNASequenceAnalysisTool
   ```

2. Install dependencies:
   ```bash
   poetry install
   ```

3. Set up pre-commit hooks:
   ```bash
   pre-commit install
   ```

## Making Changes

1. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/issue-number-description
   ```

2. Make your changes following the code style guidelines

3. Run tests to ensure everything works:
   ```bash
   poetry run pytest
   ```

4. Commit your changes with a descriptive message:
   ```bash
   git commit -m "Add feature: your feature description"
   ```

## Code Style

We use several tools to maintain code quality and style:

- **Black** for code formatting
- **isort** for import sorting
- **Flake8** for linting
- **Mypy** for type checking

These are automatically checked by pre-commit hooks. To run them manually:

```bash
poetry run black .
poetry run isort .
poetry run flake8
poetry run mypy .
```

## Testing

We use `pytest` for testing. To run the test suite:

```bash
poetry run pytest
```

For test coverage:

```bash
poetry run pytest --cov=dna_sequence_analysis_tool tests/
```

## Documentation

We use Sphinx for documentation. To build the docs locally:

```bash
cd docs
poetry run make html
```

Documentation will be available in `docs/_build/html/index.html`.

## Submitting a Pull Request

1. Push your changes to your fork:
   ```bash
   git push origin your-branch-name
   ```

2. Open a pull request against the `main` branch
3. Fill in the PR template with all relevant information
4. Ensure all CI checks pass
5. Address any review comments

## Reporting Issues

When reporting an issue, please include:

- A clear description of the issue
- Steps to reproduce
- Expected vs actual behavior
- Environment information (Python version, OS, etc.)
- Any relevant error messages or logs

## Feature Requests

We welcome feature requests! Please open an issue and use the "Feature Request" template to describe:

- The feature you'd like to see
- Why it would be useful
- Any implementation ideas you have

Thank you for contributing to the DNA Sequence Analysis Tool!
