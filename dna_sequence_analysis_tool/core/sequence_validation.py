"""
Sequence Validation Module
=========================

This module provides comprehensive validation utilities for DNA and RNA sequences.
It includes functions to validate sequence content, format, and structure according
to various biological sequence standards.

Key Features:
    - DNA/RNA sequence validation
    - IUPAC nucleotide code support
    - Sequence pair validation for alignment
    - Reading frame validation
    - Sequence length constraints

Example:
    >>> from dna_sequence_analysis_tool.core import validate_sequence
    >>> is_valid, message = validate_sequence("ATGCGATCG")
    >>> is_valid
    True
"""

from typing import Tuple, Set, Optional, Dict, Any, List, Union
from dataclasses import dataclass, field
from functools import lru_cache
import re

from ..utils.logging import logger
from ..core import SequenceValidationError, DNAToolkitError

__all__ = [
    'validate_sequence',
    'validate_rna_sequence',
    'validate_sequence_pair',
    'validate_reading_frame',
    'validate_sequence_length',
    'SequenceValidator',
    'NucleotideValidation',
    'ValidationResult'
]

class ValidationResult:
    """Container for validation results with additional context.
    
    Attributes:
        is_valid (bool): Whether the validation passed
        message (str): Description of the validation result
        details (Dict[str, Any]): Additional validation details
    """
    
    def __init__(self, is_valid: bool, message: str = "", **details: Any):
        self.is_valid = is_valid
        self.message = message
        self.details = details or {}
    
    def __bool__(self) -> bool:
        return self.is_valid
    
    def __str__(self) -> str:
        return f"{'VALID' if self.is_valid else 'INVALID'}: {self.message}"

@dataclass
class NucleotideValidation:
    """Constants and sets for nucleotide validation."""
    DNA_NUCLEOTIDES: Set[str] = frozenset('ATGC')
    RNA_NUCLEOTIDES: Set[str] = frozenset('AUGC')
    IUPAC_DNA: Set[str] = frozenset('ATGCWSMKRYBDHVN')
    IUPAC_RNA: Set[str] = frozenset('AUGCSWMRYKBDHVN')
    
    AMBIGUITY_CODES: Dict[str, Set[str]] = field(default_factory=lambda: {
        'W': {'A', 'T'}, 'S': {'G', 'C'}, 'M': {'A', 'C'}, 'K': {'G', 'T'},
        'R': {'A', 'G'}, 'Y': {'C', 'T'}, 'B': {'C', 'G', 'T'}, 'D': {'A', 'G', 'T'},
        'H': {'A', 'C', 'T'}, 'V': {'A', 'C', 'G'}, 'N': {'A', 'T', 'G', 'C'}
    })

class SequenceValidator:
    """Centralized sequence validation with configurable options."""
    
    def __init__(self, sequence_type: str = 'dna', 
                 allow_ambiguous: bool = False, 
                 case_sensitive: bool = False):
        """Initialize the sequence validator."""
        self.sequence_type = sequence_type.lower()
        self.allow_ambiguous = allow_ambiguous
        self.case_sensitive = case_sensitive
        
        if self.sequence_type == 'dna':
            self.valid_chars = (
                NucleotideValidation.IUPAC_DNA 
                if allow_ambiguous 
                else NucleotideValidation.DNA_NUCLEOTIDES
            )
        elif self.sequence_type == 'rna':
            self.valid_chars = (
                NucleotideValidation.IUPAC_RNA
                if allow_ambiguous
                else NucleotideValidation.RNA_NUCLEOTIDES
            )
        else:
            raise ValueError(f"Unsupported sequence type: {sequence_type}. Use 'dna' or 'rna'.")
    
    def validate(self, sequence: str) -> ValidationResult:
        """Validate a sequence according to the validator's configuration."""
        if not sequence:
            return ValidationResult(False, "Empty sequence")
            
        if not self.case_sensitive:
            sequence = sequence.upper()
            
        invalid_bases = set(sequence) - self.valid_chars
        
        if invalid_bases:
            return ValidationResult(
                False,
                f"Invalid {self.sequence_type.upper()} bases found: {','.join(sorted(invalid_bases))}",
                invalid_bases=sorted(invalid_bases),
                valid_bases=sorted(self.valid_chars)
            )
            
        return ValidationResult(True, "Sequence is valid")

def validate_sequence(sequence: str, allow_ambiguous: bool = False) -> Tuple[bool, str]:
    """Validate a DNA sequence.
    
    Args:
        sequence: DNA sequence to validate
        allow_ambiguous: Whether to allow IUPAC ambiguity codes
        
    Returns:
        Tuple[bool, str]: (is_valid, error_message)
    """
    validator = SequenceValidator('dna', allow_ambiguous=allow_ambiguous)
    result = validator.validate(sequence)
    return bool(result), result.message

def validate_rna_sequence(sequence: str, allow_ambiguous: bool = False) -> Tuple[bool, str]:
    """Validate an RNA sequence.
    
    Args:
        sequence: RNA sequence to validate
        allow_ambiguous: Whether to allow IUPAC ambiguity codes
        
    Returns:
        Tuple[bool, str]: (is_valid, error_message)
    """
    validator = SequenceValidator('rna', allow_ambiguous=allow_ambiguous)
    result = validator.validate(sequence)
    return bool(result), result.message

def validate_sequence_pair(seq1: str, seq2: str, **kwargs) -> Tuple[bool, str]:
    """Validate a pair of sequences for alignment.
    
    Args:
        seq1: First sequence to validate
        seq2: Second sequence to validate
        **kwargs: Additional arguments passed to validate_sequence
        
    Returns:
        Tuple[bool, str]: (is_valid, error_message)
    """
    validator = SequenceValidator('dna', **kwargs)
    result1 = validator.validate(seq1)
    if not result1:
        return False, f"First sequence: {result1.message}"
        
    result2 = validator.validate(seq2)
    if not result2:
        return False, f"Second sequence: {result2.message}"
        
    return True, ""

def validate_reading_frame(sequence: str, **kwargs) -> Tuple[bool, str]:
    """Validate sequence length for reading frame analysis.
    
    Args:
        sequence: Sequence to validate
        **kwargs: Additional arguments passed to validate_sequence
        
    Returns:
        Tuple[bool, str]: (is_valid, error_message)
    """
    validator = SequenceValidator('dna', **kwargs)
    result = validator.validate(sequence)
    if not result:
        return False, result.message
        
    if len(sequence) % 3 != 0:
        return False, "Sequence length must be divisible by 3 for reading frame analysis"
        
    return True, ""

def validate_sequence_length(sequence: str, 
                          min_length: Optional[int] = None, 
                          max_length: Optional[int] = None) -> Tuple[bool, str]:
    """Validate sequence length constraints.
    
    Args:
        sequence: Sequence to validate
        min_length: Minimum allowed sequence length
        max_length: Maximum allowed sequence length
        
    Returns:
        Tuple[bool, str]: (is_valid, error_message)
    """
    seq_len = len(sequence)
    if min_length is not None and seq_len < min_length:
        return False, f"Sequence length {seq_len} below minimum {min_length}"
    if max_length is not None and seq_len > max_length:
        return False, f"Sequence length {seq_len} above maximum {max_length}"
    return True, ""