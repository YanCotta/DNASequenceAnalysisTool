from typing import Dict, Any
import numpy as np
from concurrent.futures import ThreadPoolExecutor
from collections import Counter
from .sequence_validation import validate_sequence, SequenceValidationError
from ..utils.logging import logger

class StatisticsError(Exception):
    """Custom exception for statistics calculation errors."""
    pass

class SequenceStatistics:
    """Enhanced statistics with parallel processing for large sequences."""
    
    MOLECULAR_WEIGHTS = {
        'A': 313.21, 'T': 304.2, 'G': 329.21, 'C': 289.18,
        'U': 290.17  # For RNA
    }

    @staticmethod
    def calculate_gc_content(sequence: str) -> float:
        """Calculate GC content with validation."""
        is_valid, error_msg = validate_sequence(sequence)
        if not is_valid:
            logger.error(f"Validation failed: {error_msg}")
            raise ValueError(error_msg)
        
        sequence = sequence.upper()
        gc_count = sequence.count('G') + sequence.count('C')
        gc_content = (gc_count / len(sequence)) * 100 if sequence else 0
        logger.debug(f"GC Content calculated: {gc_content}%")
        return gc_content

    @staticmethod
    def calculate_melting_temp(sequence: str) -> float:
        """Enhanced melting temperature calculation."""
        is_valid, error_msg = validate_sequence(sequence)
        if not is_valid:
            raise ValueError(error_msg)
            
        sequence = sequence.upper()
        length = len(sequence)
        
        if length < 14:
            # Short sequence formula
            at_count = sequence.count('A') + sequence.count('T')
            gc_count = sequence.count('G') + sequence.count('C')
            return at_count * 2 + gc_count * 4
        else:
            # Long sequence formula with salt correction
            gc_fraction = (sequence.count('G') + sequence.count('C')) / length
            return 81.5 + 16.6 * np.log10(0.05) + 41 * gc_fraction - 500 / length

    @staticmethod
    def get_comprehensive_stats(sequence: str) -> Dict[str, Any]:
        """Comprehensive sequence statistics."""
        basic_stats = SequenceStatistics._get_basic_stats(sequence)
        advanced_stats = SequenceStatistics._get_advanced_stats(sequence)
        return {**basic_stats, **advanced_stats}

    @staticmethod
    def _get_basic_stats(sequence: str) -> Dict[str, Any]:
        """Basic sequence statistics."""
        sequence = sequence.upper()
        return {
            'length': len(sequence),
            'gc_content': SequenceStatistics.calculate_gc_content(sequence),
            'nucleotide_counts': Counter(sequence),
            'molecular_weight': sum(SequenceStatistics.MOLECULAR_WEIGHTS[base] 
                                for base in sequence)
        }

    @staticmethod
    def _get_advanced_stats(sequence: str) -> Dict[str, Any]:
        """Advanced sequence statistics."""
        sequence = sequence.upper()
        return {
            'dinucleotide_counts': SequenceStatistics._count_kmers(sequence, 2),
            'trinucleotide_counts': SequenceStatistics._count_kmers(sequence, 3),
            'melting_temperature': SequenceStatistics.calculate_melting_temp(sequence),
            'complexity_score': SequenceStatistics._calculate_complexity(sequence)
        }

    @staticmethod
    def _count_kmers(sequence: str, k: int) -> Dict[str, int]:
        """Count k-mers in sequence."""
        return Counter(sequence[i:i+k] for i in range(len(sequence)-k+1))

    @staticmethod
    def _calculate_complexity(sequence: str) -> float:
        """Calculate sequence complexity score."""
        k = min(len(sequence), 5)  # Use up to 5-mers
        observed_kmers = len(SequenceStatistics._count_kmers(sequence, k))
        possible_kmers = min(4**k, len(sequence)-k+1)
        return observed_kmers / possible_kmers

    @staticmethod
    def parallel_analysis(sequence: str, chunk_size: int = 1000) -> Dict[str, Any]:
        """Process large sequences in parallel chunks."""
        if len(sequence) < chunk_size:
            return SequenceStatistics.get_comprehensive_stats(sequence)
            
        chunks = [sequence[i:i+chunk_size] 
                 for i in range(0, len(sequence), chunk_size)]
        
        with ThreadPoolExecutor() as executor:
            results = list(executor.map(
                SequenceStatistics.get_comprehensive_stats, chunks))
            
        return SequenceStatistics._merge_results(results)

    @staticmethod
    def _merge_results(results: list) -> Dict[str, Any]:
        """Merge results from parallel analysis."""
        merged = results[0]
        for result in results[1:]:
            for key, value in result.items():
                if isinstance(value, dict):
                    for sub_key, sub_value in value.items():
                        merged[key][sub_key] += sub_value
                else:
                    merged[key] += value
        return merged
