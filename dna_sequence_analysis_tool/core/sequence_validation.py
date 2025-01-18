"""Sequence validation utilities."""

from typing import Tuple, Set
from dataclasses import dataclass
from ..utils.logging import logger

# Define exports explicitly at the top
__all__ = [
    'validate_sequence',
    'validate_rna_sequence',
    'validate_sequence_pair',
    'validate_reading_frame',
    'SequenceValidationError',
    'NucleotideValidation'
]

class SequenceValidationError(Exception):
    """Custom exception for sequence validation errors."""
    pass

@dataclass
class NucleotideValidation:
    """Constants and sets for nucleotide validation."""
    DNA_NUCLEOTIDES: Set[str] = frozenset('ATGC')
    RNA_NUCLEOTIDES: Set[str] = frozenset('AUGC')
    IUPAC_NUCLEOTIDES: Set[str] = frozenset('ATGCYRWSKMDVHBN')

def validate_sequence(sequence: str) -> Tuple[bool, str]:
    # Implementation for DNA sequence validation
    pass

def validate_rna_sequence(sequence: str) -> Tuple[bool, str]:
    # Implementation for RNA sequence validation
    pass

def validate_sequence_pair(seq1: str, seq2: str) -> Tuple[bool, str]:
    # Implementation for validating a pair of sequences
    pass

def validate_reading_frame(sequence: str) -> Tuple[bool, str]:
    # Implementation for validating reading frame
    pass
