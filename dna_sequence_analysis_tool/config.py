"""
Configuration settings for the DNA Sequence Analysis Tool.

This module handles all configuration settings including default values,
user preferences, and environment-based configuration.
"""
import os
from pathlib import Path
from typing import Dict, Any, Optional
import yaml
from pydantic import BaseSettings, Field, validator

# Default configuration directory
DEFAULT_CONFIG_DIR = Path.home() / ".dna_sequence_analysis"
DEFAULT_CONFIG_FILE = DEFAULT_CONFIG_DIR / "config.yaml"

# Ensure config directory exists
DEFAULT_CONFIG_DIR.mkdir(parents=True, exist_ok=True)

class Settings(BaseSettings):
    """Application settings with validation and default values."""
    
    # General settings
    log_level: str = "INFO"
    max_sequence_length: int = 10_000_000  # For safety checks
    
    # File I/O settings
    default_input_format: str = "fasta"
    default_output_format: str = "fasta"
    auto_detect_format: bool = True
    
    # Performance settings
    chunk_size: int = 10_000  # For processing large files
    max_workers: int = os.cpu_count() or 4
    
    # Visualization settings
    plot_theme: str = "default"
    default_figure_size: tuple = (10, 6)
    
    # External services
    ncbi_api_key: Optional[str] = None
    
    class Config:
        env_prefix = "DNATOOLS_"
        case_sensitive = False

# Load settings from YAML if exists
settings = Settings()

if DEFAULT_CONFIG_FILE.exists():
    try:
        with open(DEFAULT_CONFIG_FILE, 'r') as f:
            yaml_config = yaml.safe_load(f) or {}
        settings = Settings(**yaml_config)
    except Exception as e:
        import warnings
        warnings.warn(f"Error loading config file: {e}")

def save_settings():
    """Save current settings to config file."""
    with open(DEFAULT_CONFIG_FILE, 'w') as f:
        yaml.dump(settings.dict(exclude_unset=True), f, default_flow_style=False)
