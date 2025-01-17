import logging
from pathlib import Path
from typing import Dict, Union

from .logging import logger

def read_fasta(filepath: Union[str, Path]) -> Dict[str, str]:
    """
    Reads a FASTA file and returns a dictionary of sequences.
    
    Args:
        filepath: Path to the FASTA file.
        
    Returns:
        A dictionary with sequence IDs as keys and sequences as values.
    """
    logger.info(f"Reading FASTA file from {filepath}")
    filepath = Path(filepath)
    if not filepath.exists():
        logger.error(f"FASTA file not found: {filepath}")
        raise FileNotFoundError(f"FASTA file not found: {filepath}")
    
    sequences = {}
    current_id = None
    current_seq = []
    
    with open(filepath, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if current_id:
                    sequences[current_id] = ''.join(current_seq)
                    logger.debug(f"Loaded sequence {current_id}")
                current_id = line[1:].split()[0]
                current_seq = []
            else:
                current_seq.append(line.upper())
        if current_id:
            sequences[current_id] = ''.join(current_seq)
            logger.debug(f"Loaded sequence {current_id}")
    
    logger.info(f"Successfully read {len(sequences)} sequences from {filepath}")
    return sequences

def write_fasta(sequences: Dict[str, str], filepath: Union[str, Path]) -> None:
    """
    Writes sequences to a FASTA file.
    
    Args:
        sequences: A dictionary with sequence IDs as keys and sequences as values.
        filepath: Path to the output FASTA file.
    """
    logger.info(f"Writing FASTA file to {filepath}")
    filepath = Path(filepath)
    
    with open(filepath, 'w') as file:
        for seq_id, sequence in sequences.items():
            file.write(f">{seq_id}\n")
            # Write sequence in lines of max 80 characters
            for i in range(0, len(sequence), 80):
                file.write(f"{sequence[i:i+80]}\n")
            logger.debug(f"Wrote sequence {seq_id}")
    
    logger.info(f"Successfully wrote {len(sequences)} sequences to {filepath}")
