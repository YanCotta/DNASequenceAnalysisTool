"""Advanced DNA sequence analysis tools."""

from typing import List, Tuple, Dict, Any, Optional
from dataclasses import dataclass
from collections import defaultdict
import array
from functools import lru_cache

from .sequence_validation import validate_sequence, SequenceValidationError
from .sequence_transformation import SequenceTransformer
from ..utils.logging import logger

try:
    import numpy as np
    from scipy.signal import find_peaks
    NUMPY_AVAILABLE = True
except ImportError:
    logger.warning("NumPy/SciPy not available. Some advanced features will be disabled.")
    NUMPY_AVAILABLE = False

class AnalysisError(Exception):
    def __init__(self, message: str, sequence: str = None):
        self.sequence = sequence
        super().__init__(f"Analysis Error: {message}")

@dataclass
class AdvancedAnalysisParameters:
    """Enhanced parameters for sequence analysis."""
    MIN_ORF_LENGTH: int = 30
    ALIGNMENT_GAP_OPEN: float = -10.0
    ALIGNMENT_GAP_EXTEND: float = -0.5
    ALIGNMENT_MATCH_SCORE: float = 2.0
    ALIGNMENT_MISMATCH_SCORE: float = -1.0
    COMPLEXITY_WINDOW: int = 50
    MIN_REPEAT_LENGTH: int = 2

class AdvancedSequenceAnalyzer:
    """Advanced sequence analysis with modern algorithms."""
    
    @staticmethod
    def predict_promoter_regions(sequence: str) -> List[Tuple[int, float]]:
        """Predict potential promoter regions."""
        if not NUMPY_AVAILABLE:
            return []
            
        is_valid, error_msg = validate_sequence(sequence)
        if not is_valid:
            raise AnalysisError(error_msg)

        tata_box_pwm = np.array([
            [0.8, 0.1, 0.05, 0.05],  # T
            [0.9, 0.05, 0.02, 0.03], # A
            [0.1, 0.05, 0.05, 0.8],  # T
            [0.9, 0.02, 0.05, 0.03], # A
        ])
        
        sequence = sequence.upper()
        nucleotide_map = {'A': 1, 'T': 0, 'G': 2, 'C': 3}
        scores = []
        
        for i in range(len(sequence) - 3):
            window = sequence[i:i+4]
            try:
                score = sum(tata_box_pwm[j][nucleotide_map[base]] 
                        for j, base in enumerate(window))
                scores.append((i, score))
            except KeyError:
                continue
                
        return sorted([(pos, score) for pos, score in scores if score > 2.5],
                    key=lambda x: x[1], reverse=True)

    @staticmethod
    def analyze_repeats(sequence: str, params: AdvancedAnalysisParameters) -> Dict[str, Any]:
        """Advanced repeat analysis including tandem repeats."""
        if not NUMPY_AVAILABLE:
            return {"error": "NumPy required for advanced repeat analysis"}
            
        sequence = sequence.upper()
        results = {
            "tandem_repeats": [],
            "direct_repeats": defaultdict(list),
            "inverted_repeats": []
        }
        
        # Find tandem repeats using sliding windows
        for window_size in range(2, min(20, len(sequence) // 2)):
            for i in range(len(sequence) - window_size):
                pattern = sequence[i:i+window_size]
                j = i + window_size
                while j < len(sequence) - window_size + 1:
                    if sequence[j:j+window_size] == pattern:
                        results["tandem_repeats"].append({
                            "pattern": pattern,
                            "start": i,
                            "length": window_size,
                            "copies": 2
                        })
                        j += window_size
                    else:
                        break
        
        return dict(results)

    @staticmethod
    def local_alignment_affine(seq1: str, seq2: str, params: AdvancedAnalysisParameters) -> Dict[str, Any]:
        """Smith-Waterman alignment with affine gap penalties."""
        if not NUMPY_AVAILABLE:
            return {"error": "NumPy required for alignment"}
            
        m, n = len(seq1), len(seq2)
        score_matrix = np.zeros((m+1, n+1))
        pointer_matrix = np.zeros((m+1, n+1), dtype=np.int8)
        
        # Initialize matrices
        score_matrix[0, 1:] = params.ALIGNMENT_GAP_OPEN + \
                             np.arange(n) * params.ALIGNMENT_GAP_EXTEND
        score_matrix[1:, 0] = params.ALIGNMENT_GAP_OPEN + \
                             np.arange(m) * params.ALIGNMENT_GAP_EXTEND
        
        # Fill matrices
        for i in range(1, m+1):
            for j in range(1, n+1):
                match_score = params.ALIGNMENT_MATCH_SCORE if seq1[i-1] == seq2[j-1] \
                            else params.ALIGNMENT_MISMATCH_SCORE
                diagonal = score_matrix[i-1, j-1] + match_score
                vertical = score_matrix[i-1, j] + params.ALIGNMENT_GAP_EXTEND
                horizontal = score_matrix[i, j-1] + params.ALIGNMENT_GAP_EXTEND
                
                score_matrix[i, j] = max(0, diagonal, vertical, horizontal)
                
                if score_matrix[i, j] == 0:
                    pointer_matrix[i, j] = 0
                elif score_matrix[i, j] == diagonal:
                    pointer_matrix[i, j] = 1
                elif score_matrix[i, j] == vertical:
                    pointer_matrix[i, j] = 2
                else:
                    pointer_matrix[i, j] = 3
        
        return {
            "score": float(score_matrix.max()),
            "score_matrix": score_matrix.tolist(),
            "pointer_matrix": pointer_matrix.tolist()
        }

class SequenceAnalyzer:
    """Basic sequence analysis functionality."""
    
    @staticmethod
    def find_orfs(sequence: str, min_length: int = 30) -> List[Tuple[int, str, int]]:
        """Find Open Reading Frames in the sequence."""
        is_valid, error_msg = validate_sequence(sequence)
        if not is_valid:
            raise AnalysisError(error_msg)
            
        sequence = sequence.upper()
        orfs = []
        
        for frame in range(3):
            i = frame
            while i < len(sequence) - 2:
                if sequence[i:i+3] == 'ATG':  # Start codon
                    for j in range(i + 3, len(sequence) - 2, 3):
                        codon = sequence[j:j+3]
                        if codon in {'TAA', 'TAG', 'TGA'}:  # Stop codons
                            if j + 3 - i >= min_length:
                                orfs.append((i, sequence[i:j+3], frame))
                            break
                i += 3
                
        return sorted(orfs, key=lambda x: len(x[1]), reverse=True)

    @staticmethod
    @lru_cache(maxsize=128)
    def find_motifs(sequence: str, motif: str) -> List[int]:
        """Find all occurrences of a motif in the sequence."""
        sequence = sequence.upper()
        motif = motif.upper()
        return [i for i in range(len(sequence)-len(motif)+1) 
                if sequence[i:i+len(motif)] == motif]
