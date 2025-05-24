"""
DNA Sequence Analysis Tool - Core Module
======================================

This module provides comprehensive tools for DNA/RNA sequence manipulation, analysis,
and bioinformatics tasks. It's designed to be both performant and easy to use for
both simple sequence analysis and complex bioinformatics workflows.

Key Features:
    - Sequence validation and sanitization
    - Statistical analysis of sequences
    - Sequence transformation and manipulation
    - Advanced sequence analysis (motif finding, ORF detection, etc.)
    - High-performance implementations for large sequences

Example:
    >>> from dna_sequence_analysis_tool import DNAToolkit
    >>> toolkit = DNAToolkit()
    >>> analysis = toolkit.analyze_sequence("ATGCGATCGATCGATCGATCG")
    >>> print(f"GC Content: {analysis.gc_content:.2f}%")
"""

# Custom exceptions
class DNAToolkitError(Exception):
    """Base exception for all DNA Toolkit exceptions."""
    pass

class SequenceValidationError(DNAToolkitError):
    """Raised when a sequence fails validation."""
    pass

class FileFormatError(DNAToolkitError):
    """Raised when there's an error parsing a file format."""
    pass

class AnalysisError(DNAToolkitError):
    """Raised when an error occurs during sequence analysis."""
    pass

# Core imports
from .sequence_validation import (
    validate_sequence,
    validate_rna_sequence,
    validate_sequence_pair,
    validate_reading_frame,
    SequenceValidationError as _SequenceValidationError
)

from .sequence_transformation import SequenceTransformer
from .sequence_statistics import SequenceStatistics
from .sequence_analysis import SequenceAnalyzer, AdvancedSequenceAnalyzer
from .main import DNAToolkit

# Update __all__ to include new exceptions
__version__ = "1.0.0"
__all__ = [
    # Core functionality
    'DNAToolkit',
    'SequenceTransformer',
    'SequenceStatistics',
    'SequenceAnalyzer',
    'AdvancedSequenceAnalyzer',
    
    # Validation functions
    'validate_sequence',
    'validate_rna_sequence',
    'validate_sequence_pair',
    'validate_reading_frame',
    
    # Exceptions
    'DNAToolkitError',
    'SequenceValidationError',
    'FileFormatError',
    'AnalysisError'
]
