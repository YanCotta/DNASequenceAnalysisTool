"""DNA sequence statistics calculations."""

from collections import Counter
import math
from typing import Dict, Any
from functools import lru_cache

class SequenceStatistics:
    @lru_cache(maxsize=128)
    def get_comprehensive_stats(self, sequence: str) -> dict:
        """Calculate comprehensive sequence statistics with caching."""
        sequence = sequence.upper()
        counts = Counter(sequence)
        gc_count = counts.get('G', 0) + counts.get('C', 0)
        length = len(sequence)
        gc_content = (gc_count / length * 100) if length else 0
        
        # More accurate molecular weights including phosphate backbone
        base_weights = {
            'A': 331.2218,  # dAMP
            'T': 322.2085,  # dTMP
            'G': 347.2212,  # dGMP
            'C': 307.1971   # dCMP
        }
        # Add weight of phosphodiester bonds
        molecular_weight = sum(base_weights.get(base, 0) for base in sequence)
        if length > 1:
            molecular_weight -= (length - 1) * 61.96  # Subtract water loss from phosphodiester bonds
            
        dinucleotides = self._calculate_dinucleotide_freq(sequence)
        
        return {
            'gc_content': gc_content,
            'nucleotide_counts': dict(counts),
            'molecular_weight': molecular_weight,
            'dinucleotide_frequencies': dinucleotides,
            'sequence_entropy': self._calculate_entropy(counts, length)
        }

    def _calculate_complexity(self, sequence: str) -> float:
        """Calculate sequence complexity using k-mer entropy."""
        length = len(sequence)
        if not length:
            return 0.0
        counts = Counter(sequence)
        return self._calculate_entropy(counts, length)

    def _calculate_entropy(self, counts: Counter, length: int) -> float:
        """Calculate Shannon entropy from nucleotide frequencies."""
        entropy = 0.0
        for count in counts.values():
            p = count / length
            entropy -= p * math.log2(p) if p > 0 else 0
        return entropy

    def _calculate_dinucleotide_freq(self, sequence: str) -> Dict[str, float]:
        """Calculate dinucleotide frequencies."""
        if len(sequence) < 2:
            return {}
            
        dinucleotides = Counter(sequence[i:i+2] for i in range(len(sequence)-1))
        total = sum(dinucleotides.values())
        return {k: v/total for k, v in dinucleotides.items()}
