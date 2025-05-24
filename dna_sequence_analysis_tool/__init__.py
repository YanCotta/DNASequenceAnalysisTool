"""
DNA Sequence Analysis Tool
=========================

A comprehensive Python toolkit for DNA sequence analysis, manipulation, and visualization.
"""

from .cli import cli
from .core.sequence_analysis import SequenceAnalyzer, AdvancedSequenceAnalyzer
from .core.sequence_io import read_sequence_file, write_sequence_file
from .core.sequence_validation import validate_sequence
from .core.visualization import plot_gc_content, plot_sequence_logo
from .data.sample_sequence import get_sample_dna, get_sample_rna, get_test_sequences

__version__ = "0.1.0"
__all__ = [
    'cli',
    'SequenceAnalyzer',
    'AdvancedSequenceAnalyzer',
    'read_sequence_file',
    'write_sequence_file',
    'validate_sequence',
    'plot_gc_content',
    'plot_sequence_logo',
    'get_sample_dna',
    'get_sample_rna',
    'get_test_sequences',
]
