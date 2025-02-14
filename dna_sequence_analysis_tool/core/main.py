"""Main module for DNA sequence analysis toolkit."""

from typing import Tuple, List, Dict, Optional, Union
from dataclasses import dataclass
from functools import lru_cache

try:
    import numpy as np
    NUMPY_AVAILABLE = True
except ImportError:
    NUMPY_AVAILABLE = False

from .sequence_validation import validate_sequence
from .sequence_statistics import SequenceStatistics
from .sequence_transformation import SequenceTransformer
from .sequence_analysis import AdvancedSequenceAnalyzer, SequenceAnalyzer
from ..utils.logging import logger

@dataclass
class DNAStats:
    """Data class for storing DNA sequence statistics."""
    length: int
    gc_content: float
    nucleotide_counts: Dict[str, int]
    complexity: float
    repeats: Dict[str, List[int]]
    molecular_weight: float

class DNAToolkit:
    """Main interface for DNA sequence analysis tools."""
    
    def __init__(self):
        self.stats = SequenceStatistics()
        self.transformer = SequenceTransformer()
        self.basic_analyzer = SequenceAnalyzer()
        self.advanced_analyzer = AdvancedSequenceAnalyzer()
    
    @staticmethod
    @lru_cache(maxsize=1024)
    def validate_sequence(sequence: str) -> Tuple[bool, str]:
        """Cached validation for better performance."""
        return validate_sequence(sequence)

    def analyze_sequence(self, sequence: str, window_size: Optional[int] = None) -> DNAStats:
        """Comprehensive sequence analysis."""
        try:
            is_valid, error_msg = self.validate_sequence(sequence)
            if not is_valid:
                raise ValueError(error_msg)
                
            basic_stats = self.stats.get_comprehensive_stats(sequence)
            
            # Basic repeats using SequenceAnalyzer if numpy is not available
            if not NUMPY_AVAILABLE:
                repeats = {motif: positions for motif, positions 
                        in self.basic_analyzer.find_repeats(sequence).items()}
            else:
                repeats = self.advanced_analyzer.analyze_repeats(
                    sequence, 
                    window_size or 50
                ).get("direct_repeats", {})
            
            complexity = self.stats._calculate_complexity(sequence)
            
            return DNAStats(
                length=len(sequence),
                gc_content=basic_stats['gc_content'],
                nucleotide_counts=basic_stats['nucleotide_counts'],
                complexity=complexity,
                repeats=repeats,
                molecular_weight=basic_stats['molecular_weight']
            )
            
        except Exception as e:
            logger.error(f"Error analyzing sequence: {str(e)}")
            raise

def main():
    """Demonstrates the DNA sequence analysis toolkit functionality."""
    try:
        toolkit = DNAToolkit()
        sample_dna = "AGCTATCGGCTAGCG"
        
        logger.info("\nDNA Sequence Analysis Results")
        logger.info("-" * 30)
        logger.info(f"Sequence: {sample_dna}")
        
        # Analyze sequence
        analysis = toolkit.analyze_sequence(sample_dna)
        
        # Display results
        logger.info(f"\nSequence Statistics:")
        logger.info(f"Length: {analysis.length}")
        logger.info(f"GC Content: {analysis.gc_content:.2f}%")
        logger.info("Nucleotide Counts:")
        for base, count in analysis.nucleotide_counts.items():
            logger.info(f"  {base}: {count}")
        logger.info(f"Sequence Complexity: {analysis.complexity:.3f}")
        logger.info(f"Molecular Weight: {analysis.molecular_weight:.2f}")
        
        if analysis.repeats:
            logger.info("\nRepeated Sequences:")
            for pattern, positions in analysis.repeats.items():
                logger.info(f"  {pattern}: {positions}")
        
    except ValueError as e:
        logger.error(f"Validation error: {e}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
