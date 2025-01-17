"""Sample sequence provider with validation and common genetic elements."""

from typing import Dict, List, Union, Optional
from pathlib import Path
from ..core.sequence_validation import validate_sequence, SequenceValidationError
from ..utils.file_io import read_fasta
from ..utils.logging import logger

# Common genetic elements for testing
SAMPLE_SEQUENCES = {
    'promoter': 'TATAAT',  # bacterial promoter
    'start_codon': 'ATG',
    'stop_codon': 'TAA',
    'kozak': 'GCCACCATGG',  # eukaryotic translation initiation
    'test_dna': 'ATGCGATCGTAGCTAGCTAGCTGATCGATCG',
    'test_rna': 'AUGCGAUCGUAGCUAGCUAGCUGAUCGAUCG',
    'gc_rich': 'GCGCGCGCGCGCGC',
    'at_rich': 'ATATATATATAT'
}

class SampleDataError(Exception):
    """Custom exception for sample data errors."""
    pass

def get_sample_dna(sequence_type: str = 'test_dna') -> str:
    """
    Get a sample DNA sequence by type.
    
    Args:
        sequence_type: Type of sequence to return
        
    Returns:
        Sample sequence string
    
    Raises:
        SampleDataError: If sequence type is invalid
    """
    if sequence_type not in SAMPLE_SEQUENCES:
        raise SampleDataError(f"Unknown sequence type: {sequence_type}")
    return SAMPLE_SEQUENCES[sequence_type]

def get_sample_rna(sequence_type: str = 'test_rna') -> str:
    """Get a sample RNA sequence."""
    if sequence_type not in SAMPLE_SEQUENCES:
        raise SampleDataError(f"Unknown sequence type: {sequence_type}")
    return SAMPLE_SEQUENCES[sequence_type]

def get_test_sequences() -> Dict[str, str]:
    """Get all available test sequences."""
    return SAMPLE_SEQUENCES.copy()

def load_fasta_sequence(filepath: Union[str, Path]) -> Dict[str, str]:
    logger.info(f"Loading FASTA sequence from {filepath}")
    try:
        sequences = read_fasta(filepath)
        logger.info(f"Loaded {len(sequences)} sequences from {filepath}")
        return sequences
    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
        raise SampleDataError(str(e))
    except SequenceValidationError as e:
        logger.error(f"Validation error: {e}")
        raise SampleDataError(str(e))
