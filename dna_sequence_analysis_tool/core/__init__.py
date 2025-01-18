"""
Core DNA sequence analysis functionality.
Provides tools for DNA/RNA sequence manipulation and analysis.
"""

from .sequence_validation import validate_sequence, validate_rna_sequence, validate_sequence_pair, validate_reading_frame
from .sequence_transformation import SequenceTransformer
from .sequence_statistics import SequenceStatistics
from .sequence_analysis import SequenceAnalyzer, AdvancedSequenceAnalyzer
from .main import DNAToolkit

__version__ = "1.0.0"
__all__ = [
    'validate_sequence',
    'validate_rna_sequence',
    'validate_sequence_pair',
    'validate_reading_frame',
    'SequenceTransformer',
    'SequenceStatistics',
    'SequenceAnalyzer',
    'AdvancedSequenceAnalyzer',
    'DNAToolkit'
]
