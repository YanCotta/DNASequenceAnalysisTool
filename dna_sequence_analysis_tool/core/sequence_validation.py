"""Sequence validation utilities."""

from typing import Tuple, Set
from dataclasses import dataclass
from ..utils.logging import logger

class SequenceValidationError(Exception):
    """Custom exception for sequence validation errors."""
    pass

@dataclass
class NucleotideValidation:
    """Constants and sets for nucleotide validation."""
    DNA_NUCLEOTIDES: Set[str] = frozenset('ATGC')
    RNA_NUCLEOTIDES: Set[str] = frozenset('AUGC')
    IUPAC_NUCLEOTIDES: Set[str] = frozenset('ATGCYRWSKMDVHBN')

def validate_sequence(sequence: str, sequence_type: str = 'DNA') -> Tuple[bool, str]:
    """Enhanced validation with better error messages."""
    if not isinstance(sequence, str):
        logger.error(f"Invalid type for sequence: {type(sequence)}")
        return False, f"Expected string, got {type(sequence)}"
    if not sequence:
        logger.error("Empty sequence provided")
        return False, "Empty sequence provided"
    
    sequence = sequence.upper()
    valid_set = {
        'DNA': NucleotideValidation.DNA_NUCLEOTIDES,
        'RNA': NucleotideValidation.RNA_NUCLEOTIDES,
        'IUPAC': NucleotideValidation.IUPAC_NUCLEOTIDES
    }.get(sequence_type.upper())
    
    if not valid_set:
        logger.error(f"Invalid sequence type: {sequence_type}")
        return False, f"Invalid sequence type: {sequence_type}"
    
    invalid_chars = set(sequence) - valid_set
    if invalid_chars:
        logger.error(f"Invalid {sequence_type} nucleotides found: {', '.join(sorted(invalid_chars))}")
        return False, f"Invalid {sequence_type} nucleotides found: {', '.join(sorted(invalid_chars))}"
        
    logger.debug(f"Sequence {sequence_type} validation passed.")
    return True, ""

def validate_reading_frame(frame: int) -> bool:
    """Validates if reading frame is 0, 1, or 2."""
    return frame in (0, 1, 2)

def validate_sequence_pair(seq1: str, seq2: str) -> Tuple[bool, str]:
    """Validates a pair of sequences for alignment."""
    if len(seq1) != len(seq2):
        return False, "Sequences must be of equal length"
    
    valid1, msg1 = validate_sequence(seq1)
    if not valid1:
        return False, f"First sequence: {msg1}"
    
    valid2, msg2 = validate_sequence(seq2)
    if not valid2:
        return False, f"Second sequence: {msg2}"
        
    return True, ""
