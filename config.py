from dataclasses import dataclass
from typing import Dict

@dataclass
class AnalysisConfig:
    """Global configuration for analysis parameters."""
    MIN_ORF_LENGTH: int = 30
    GC_CONTENT_WINDOW: int = 100
    ALIGNMENT_PARAMS: Dict[str, float] = {
        'gap_open': -10.0,
        'gap_extend': -0.5,
        'match': 2.0,
        'mismatch': -1.0
    }