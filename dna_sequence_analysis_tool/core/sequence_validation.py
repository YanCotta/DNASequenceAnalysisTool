"""Sequence validation utilities."""

from typing import Tuple, Set
from typing import Optional
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
    """Validate a DNA sequence.
    
    Args:
        sequence (str): DNA sequence to validate
        
    Returns:
        Tuple[bool, str]: (is_valid, error_message)
    """
    if not sequence:
        return False, "Empty sequence"
        
    sequence = sequence.upper()
    invalid_bases = set(sequence) - NucleotideValidation.DNA_NUCLEOTIDES
    
    if invalid_bases:
        return False, f"Invalid DNA bases found: {','.join(invalid_bases)}"
    return True, ""

def validate_rna_sequence(sequence: str) -> Tuple[bool, str]:
    """Validate an RNA sequence."""
    if not sequence:
        return False, "Empty sequence"
        
    sequence = sequence.upper()
    invalid_bases = set(sequence) - NucleotideValidation.RNA_NUCLEOTIDES
    
    if invalid_bases:
        return False, f"Invalid RNA bases found: {','.join(invalid_bases)}"
    return True, ""

def validate_sequence_pair(seq1: str, seq2: str) -> Tuple[bool, str]:
    """Validate a pair of sequences for alignment."""
    valid1, msg1 = validate_sequence(seq1)
    if not valid1:
        return False, f"First sequence: {msg1}"
        
    valid2, msg2 = validate_sequence(seq2)
    if not valid2:
        return False, f"Second sequence: {msg2}"
        
    return True, ""

def validate_reading_frame(sequence: str) -> Tuple[bool, str]:
    """Validate sequence length for reading frame analysis."""
    valid, msg = validate_sequence(sequence)
    if not valid:
        return False, msg
        
    if len(sequence) % 3 != 0:
        return False, "Sequence length must be divisible by 3 for reading frame analysis"
        
    return True, ""

def validate_sequence_length(sequence: str, min_length: Optional[int] = None, 
                        max_length: Optional[int] = None) -> Tuple[bool, str]:
    """Validate sequence length constraints."""
    if min_length and len(sequence) < min_length:
        return False, f"Sequence length {len(sequence)} below minimum {min_length}"
    if max_length and len(sequence) > max_length:
        return False, f"Sequence length {len(sequence)} above maximum {max_length}"
    return True, ""