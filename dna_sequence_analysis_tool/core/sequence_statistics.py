from collections import Counter
import math

class SequenceStatistics:
    def get_comprehensive_stats(self, sequence: str) -> dict:
        sequence = sequence.upper()
        counts = Counter(sequence)
        gc_count = counts.get('G', 0) + counts.get('C', 0)
        length = len(sequence)
        gc_content = (gc_count / length * 100) if length else 0
        base_weights = {'A': 331.2218, 'T': 322.2085, 'G': 347.2212, 'C': 307.1971}
        molecular_weight = sum(base_weights.get(base, 0) for base in sequence)
        return {
            'gc_content': gc_content,
            'nucleotide_counts': dict(counts),
            'molecular_weight': molecular_weight
        }

    def _calculate_complexity(self, sequence: str) -> float:
        sequence = sequence.upper()
        length = len(sequence)
        if not length:
            return 0.0
        counts = Counter(sequence)
        complexity = 0.0
        for base_count in counts.values():
            p = base_count / length
            complexity -= p * math.log2(p)
        return complexity
