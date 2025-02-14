"""DNA/RNA sequence transformation utilities."""

from typing import Dict, List, Optional
from .sequence_validation import validate_sequence, validate_rna_sequence, SequenceValidationError
from ..utils.logging import logger

class TransformationError(Exception):
    """Custom exception for transformation errors."""
    pass

from dataclasses import dataclass

@dataclass
class GeneticCode:
    """Standard genetic code mapping."""
    RNA_CODONS: Dict[str, str] = {
        'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',
        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',
        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }
    START_CODON: str = 'AUG'
    STOP_CODONS: List[str] = ['UAA', 'UAG', 'UGA']

class SequenceTransformer:
    """
    Handles DNA/RNA sequence transformations.
    
    Attributes:
        None
    
    Methods:
        reverse_complement: Returns reverse complement of DNA sequence
        transcribe: Converts DNA to RNA
        translate: Converts RNA to protein sequence
    """
    @staticmethod
    def reverse_complement(sequence: str) -> str:
        """Returns reverse complement with enhanced validation."""
        is_valid, error_msg = validate_sequence(sequence)
        if not is_valid:
            logger.error(f"Validation failed: {error_msg}")
            raise SequenceValidationError(error_msg)
        
        complement_map = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
        reverse_comp = ''.join(complement_map.get(base, base) for base in sequence.upper()[::-1])
        logger.debug(f"Reverse complement of {sequence} is {reverse_comp}")
        return reverse_comp

    @staticmethod
    def transcribe(dna_sequence: str) -> str:
        """DNA to RNA transcription with validation."""
        is_valid, error_msg = validate_sequence(dna_sequence)
        if not is_valid:
            raise ValueError(error_msg)
        return dna_sequence.upper().replace('T', 'U')

    @staticmethod
    def translate(rna_sequence: str, genetic_code: Dict[str, str] = None) -> str:
        """Enhanced translation with custom genetic code support."""
        is_valid, error_msg = validate_rna_sequence(rna_sequence)
        if not is_valid:
            raise ValueError(error_msg)
        
        if genetic_code is None:
            genetic_code = GeneticCode.RNA_CODONS
            
        protein = []
        for i in range(0, len(rna_sequence)-2, 3):
            codon = rna_sequence[i:i+3]
            if len(codon) == 3:
                amino_acid = genetic_code.get(codon, 'X')
                if amino_acid == '*':
                    break
                protein.append(amino_acid)
        
        return ''.join(protein)
