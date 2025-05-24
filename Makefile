.PHONY: help install test lint format check-format type-check clean

# Default target
help:
	@echo "Please use 'make <target>', where <target> is one of:"
	@echo "  install     install package and development dependencies"
	@echo "  test        run tests quickly with the default Python"
	@echo "  lint        check code style with flake8 and black"
	@echo "  format      format code with black and isort"
	@echo "  type-check  run type checking with mypy"
	@echo "  clean       remove build and Python file artifacts"

install:
	pip install -e .
	pip install -r requirements-dev.txt
	pre-commit install

test:
	pytest -v --cov=dna_sequence_analysis_tool --cov-report=term-missing

lint:
	flake8 dna_sequence_analysis_tool tests
	black --check --diff dna_sequence_analysis_tool tests
	isort --check-only --diff dna_sequence_analysis_tool tests

format:
	black dna_sequence_analysis_tool tests
	isort dna_sequence_analysis_tool tests

type-check:
	mypy dna_sequence_analysis_tool

clean:
	rm -rf build/ dist/ .eggs/ .pytest_cache/ .mypy_cache/ .coverage htmlcov/ *.egg-info
	find . -name '*.pyc' -exec rm -f {} \;
	find . -name '*.pyo' -exec rm -f {} \;
	find . -name '*~' -exec rm -f {} \;
	find . -name '__pycache__' -exec rm -fr {} \;
