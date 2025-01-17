"""
Sample DNA/RNA sequence data and loading utilities.
Provides test sequences and common genetic elements for analysis.
"""

from .sample_sequence import (
    get_sample_dna,
    get_sample_rna,
    get_test_sequences,
    load_fasta_sequence
)

__version__ = "1.0.0"
__all__ = [
    'get_sample_dna',
    'get_sample_rna',
    'get_test_sequences',
    'load_fasta_sequence'
]
