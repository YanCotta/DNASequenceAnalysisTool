"""
Custom exceptions for the DNA Sequence Analysis Tool.

This module defines all custom exceptions used throughout the application.
"""
from typing import Optional, List, Dict, Any

class DNAToolError(Exception):
    """Base exception for all DNA Sequence Analysis Tool errors."""
    def __init__(self, message: str = "An error occurred in DNA Sequence Analysis Tool"):
        self.message = message
        super().__init__(self.message)

class SequenceError(DNAToolError):
    """Base class for sequence-related errors."""
    def __init__(self, message: str = "Invalid sequence"):
        super().__init__(message)

class InvalidSequenceError(SequenceError):
    """Raised when a sequence contains invalid characters."""
    def __init__(self, sequence: str, invalid_chars: set):
        message = f"Sequence contains invalid characters: {', '.join(sorted(invalid_chars))}"
        self.sequence = sequence
        self.invalid_chars = invalid_chars
        super().__init__(message)

class EmptySequenceError(SequenceError):
    """Raised when a sequence is empty."""
    pass

class FileError(DNAToolError):
    """Base class for file-related errors."""
    def __init__(self, message: str, path: Optional[str] = None):
        self.path = path
        super().__init__(f"{message}: {path}" if path else message)

class FileFormatError(FileError):
    """Raised when there's an error with the file format."""
    def __init__(self, message: str, path: Optional[str] = None, format: Optional[str] = None):
        self.format = format
        super().__init__(f"Invalid {format} format: {message}" if format else f"Invalid file format: {message}", path)

class ConfigurationError(DNAToolError):
    """Raised when there's a configuration error."""
    def __init__(self, message: str, config_key: Optional[str] = None):
        self.config_key = config_key
        super().__init__(f"Configuration error: {message}")

class NCBIError(DNAToolError):
    """Raised when there's an error with NCBI services."""
    def __init__(self, message: str, status_code: Optional[int] = None):
        self.status_code = status_code
        super().__init__(f"NCBI Error: {message}")

class ValidationError(DNAToolError):
    """Raised when validation fails."""
    def __init__(self, message: str, errors: Optional[Dict[str, Any]] = None):
        self.errors = errors or {}
        super().__init__(message)

class PerformanceWarning(Warning):
    """Warning for performance-related issues."""
    pass
