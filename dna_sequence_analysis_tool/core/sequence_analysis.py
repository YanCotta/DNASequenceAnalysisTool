"""Advanced DNA sequence analysis tools."""

from typing import List, Tuple, Dict, Any, Optional
from dataclasses import dataclass
import numpy as np
from functools import lru_cache
from .sequence_validation import validate_sequence, SequenceValidationError
from .sequence_transformation import SequenceTransformer
from ..utils.logging import logger

class AnalysisError(Exception):
    """Custom exception for analysis errors."""
    pass

@lru_cache(maxsize=128)
def cached_analysis(sequence: str) -> Dict[str, Any]:
    """Cache expensive analysis operations."""
    # ...existing code...

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
        """Predict potential promoter regions using position weight matrices.
        
        Args:
            sequence (str): DNA sequence to analyze.
        
        Returns:
            List[Tuple[int, float]]: List of tuples with position and score of predicted promoter regions.
        
        Raises:
            AnalysisError: If the sequence is invalid.
        """
        tata_box_pwm = np.array([
            [0.8, 0.1, 0.05, 0.05],  # T
            [0.9, 0.05, 0.02, 0.03], # A
            [0.1, 0.05, 0.05, 0.8],  # T
            [0.9, 0.02, 0.05, 0.03], # A
        ])
        
        # Implementation of promoter prediction
        # ...existing code...

    @staticmethod
    def analyze_repeats(sequence: str, params: AdvancedAnalysisParameters) -> Dict[str, Any]:
        """Advanced repeat analysis including tandem repeats.
        
        Args:
            sequence (str): DNA sequence to analyze.
            params (AdvancedAnalysisParameters): Parameters for the analysis.
        
        Returns:
            Dict[str, Any]: Analysis results.
        
        Raises:
            AnalysisError: If the sequence is invalid.
        """
        sequence = sequence.upper()
        
        from scipy.signal import find_peaks
        def find_tandem_repeats():
            """Find tandem repeats using Fourier transform."""
            signal = np.array([{'A':0, 'T':1, 'G':2, 'C':3}[base] for base in sequence])
            frequencies = np.fft.fft(signal)
            peaks, _ = find_peaks(np.abs(frequencies))
            return peaks

        # Implementation continues...
        # ...existing code...

    @staticmethod
    def local_alignment_affine(seq1: str, seq2: str, params: AdvancedAnalysisParameters) -> Dict[str, Any]:
        """Improved local alignment with affine gap penalties.
        
        Args:
            seq1 (str): First sequence.
            seq2 (str): Second sequence.
            params (AdvancedAnalysisParameters): Parameters for the alignment.
        
        Returns:
            Dict[str, Any]: Alignment results.
        
        Raises:
            AnalysisError: If the sequences are invalid.
        """
        m, n = len(seq1), len(seq2)
        score_matrix = np.zeros((m+1, n+1))
        gap_matrix = np.zeros((m+1, n+1))
        
        # Implementation of advanced alignment
        # ...existing code...

@dataclass
class AnalysisParameters:
    """Parameters for sequence analysis."""
    MIN_ORF_LENGTH: int = 30
    ALIGNMENT_GAP_PENALTY: float = -2.0
    ALIGNMENT_MATCH_SCORE: float = 1.0
    ALIGNMENT_MISMATCH_SCORE: float = -1.0

class SequenceAnalyzer:
    """Advanced sequence analysis tools."""
    
    @staticmethod
    def find_orfs(sequence: str, min_length: int = AnalysisParameters.MIN_ORF_LENGTH) -> List[Tuple[int, str, int]]:
        """Enhanced ORF finding with multiple reading frames.
        
        Args:
            sequence (str): DNA sequence to analyze.
            min_length (int): Minimum length of ORFs.
        
        Returns:
            List[Tuple[int, str, int]]: List of tuples with start position, ORF sequence, and reading frame.
        
        Raises:
            AnalysisError: If the sequence is invalid.
        """
        is_valid, error_msg = validate_sequence(sequence)
        if not is_valid:
            raise AnalysisError(error_msg)
        
        sequence = sequence.upper()
        orfs = []
        
        for frame in range(3):
            frame_orfs = SequenceAnalyzer._find_frame_orfs(sequence[frame:], frame, min_length)
            orfs.extend(frame_orfs)
            
        return sorted(orfs, key=lambda x: len(x[1]), reverse=True)

    @staticmethod
    def local_alignment(seq1: str, seq2: str) -> Dict[str, Any]:
        """Smith-Waterman local alignment.
        
        Args:
            seq1 (str): First sequence.
            seq2 (str): Second sequence.
        
        Returns:
            Dict[str, Any]: Alignment results.
        
        Raises:
            AnalysisError: If the sequences are invalid.
        """
        # Implementation of Smith-Waterman algorithm
        # ...existing alignment code...

    @staticmethod
    def find_repeats(sequence: str, min_length: int = 2) -> Dict[str, List[int]]:
        """Find repeated sequences.
        
        Args:
            sequence (str): DNA sequence to analyze.
            min_length (int): Minimum length of repeats.
        
        Returns:
            Dict[str, List[int]]: Dictionary of repeated sequences and their positions.
        
        Raises:
            AnalysisError: If the sequence is invalid.
        """
        is_valid, error_msg = validate_sequence(sequence)
        if not is_valid:
            raise AnalysisError(error_msg)
            
        sequence = sequence.upper()
        repeats = {}
        
        for length in range(min_length, len(sequence)//2 + 1):
            for i in range(len(sequence) - length + 1):
                pattern = sequence[i:i+length]
                positions = SequenceAnalyzer._find_pattern_positions(sequence, pattern)
                if len(positions) > 1:
                    repeats[pattern] = positions
                    
        return repeats

    @staticmethod
    def _find_frame_orfs(sequence: str, frame: int, min_length: int) -> List[Tuple[int, str, int]]:
        """Find ORFs in a specific reading frame."""
        orfs = []
        start_codon = 'ATG'
        stop_codons = {'TAA', 'TAG', 'TGA'}
        
        i = 0
        while i < len(sequence)-2:
            if sequence[i:i+3] == start_codon:
                for j in range(i+3, len(sequence)-2, 3):
                    codon = sequence[j:j+3]
                    if codon in stop_codons:
                        orf = sequence[i:j+3]
                        if len(orf) >= min_length:
                            orfs.append((i, orf, frame))
                        break
            i += 3
        return orfs

    @staticmethod
    def _find_pattern_positions(sequence: str, pattern: str) -> List[int]:
        """Find all positions of a pattern in sequence."""
        positions = []
        for i in range(len(sequence) - len(pattern) + 1):
            if sequence[i:i+len(pattern)] == pattern:
                positions.append(i)
        return positions
