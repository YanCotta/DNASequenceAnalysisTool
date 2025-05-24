"""
Logging configuration for the DNA Sequence Analysis Tool.

This module sets up logging with appropriate formatting and handlers.
"""
import logging
import logging.handlers
import sys
from pathlib import Path
from typing import Optional

from .config import settings, DEFAULT_CONFIG_DIR

# Configure logging
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_LEVEL = getattr(logging, settings.log_level.upper(), logging.INFO)
LOG_FILE = DEFAULT_CONFIG_DIR / "dna_analysis.log"

# Create logs directory if it doesn't exist
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

def get_logger(name: str = "dna_sequence_analysis") -> logging.Logger:
    """
    Get a configured logger instance.
    
    Args:
        name: Logger name (usually __name__)
        
    Returns:
        Configured logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(LOG_LEVEL)
    
    # Don't add handlers if they're already configured
    if logger.handlers:
        return logger
    
    # Create formatter
    formatter = logging.Formatter(LOG_FORMAT)
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # File handler with rotation (10MB per file, keep 5 backups)
    file_handler = logging.handlers.RotatingFileHandler(
        LOG_FILE,
        maxBytes=10*1024*1024,  # 10MB
        backupCount=5,
        encoding='utf-8'
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger

# Configure root logger
get_logger()
