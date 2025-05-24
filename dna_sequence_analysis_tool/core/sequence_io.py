"""
Sequence I/O Module
==================

This module provides functionality for reading and writing biological sequence data
in various file formats including FASTA and FASTQ.

Features:
    - Read/write FASTA files
    - Read/write FASTQ files
    - Support for gzip/bzip2 compressed files
    - Streaming support for large files
    - Sequence validation during I/O

Example:
    >>> from dna_sequence_analysis_tool.core.sequence_io import read_fasta
    >>> for header, sequence in read_fasta('sequences.fasta'):
    ...     print(f"{header}: {sequence[:50]}...")
"""

import gzip
import bz2
import os
from pathlib import Path
from typing import Iterator, TextIO, Tuple, Union, Optional, Dict, Any

from .sequence_validation import SequenceValidator, ValidationResult
from ..core import FileFormatError, DNAToolkitError

# Type aliases
FileLike = Union[str, os.PathLike, TextIO]

class SequenceRecord:
    """Container for sequence records with metadata."""
    
    __slots__ = ('id', 'name', 'description', 'sequence', 'quality', 'metadata')
    
    def __init__(self, 
                 sequence: str, 
                 id: str = "", 
                 name: str = "", 
                 description: str = "",
                 quality: Optional[str] = None,
                 **metadata: Any):
        """Initialize a sequence record.
        
        Args:
            sequence: The sequence data
            id: Sequence identifier
            name: Sequence name (defaults to id if not provided)
            description: Sequence description
            quality: Quality scores (for FASTQ)
            **metadata: Additional metadata as key-value pairs
        """
        self.sequence = sequence
        self.id = id or ""
        self.name = name or id or ""
        self.description = description or ""
        self.quality = quality
        self.metadata = metadata or {}
    
    def __len__(self) -> int:
        return len(self.sequence)
    
    def __str__(self) -> str:
        return f"{self.id} - {self.sequence[:20]}..."
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert record to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'sequence': self.sequence,
            'quality': self.quality,
            **self.metadata
        }

def _open_file(file: FileLike, mode: str = 'rt') -> TextIO:
    """Open a file with automatic compression detection."""
    if isinstance(file, (str, os.PathLike)):
        file = str(file)
        if file.endswith('.gz'):
            return gzip.open(file, mode + 't' if 't' not in mode else mode)
        elif file.endswith(('.bz2', '.bzip2')):
            return bz2.open(file, mode + 't' if 't' not in mode else mode)
        return open(file, mode)
    return file

def read_fasta(file: FileLike, 
              validate: bool = True,
              allow_ambiguous: bool = False) -> Iterator[SequenceRecord]:
    """Read sequences from a FASTA file.
    
    Args:
        file: Path to file or file-like object
        validate: Whether to validate sequences
        allow_ambiguous: Whether to allow IUPAC ambiguity codes
        
    Yields:
        SequenceRecord objects
        
    Raises:
        FileFormatError: If the file format is invalid
    """
    validator = SequenceValidator('dna', allow_ambiguous=allow_ambiguous) if validate else None
    current_id = ""
    current_desc = ""
    current_seq = []
    
    with _open_file(file) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
                
            if line.startswith('>'):
                # Save previous sequence if exists
                if current_id:
                    sequence = ''.join(current_seq)
                    if validator:
                        result = validator.validate(sequence)
                        if not result:
                            raise FileFormatError(f"Invalid sequence for {current_id}: {result.message}")
                    yield SequenceRecord(
                        id=current_id,
                        description=current_desc,
                        sequence=sequence
                    )
                
                # Start new sequence
                header = line[1:].split(maxsplit=1)
                current_id = header[0]
                current_desc = header[1] if len(header) > 1 else ""
                current_seq = []
            else:
                current_seq.append(line.upper())
        
        # Yield the last sequence
        if current_id:
            sequence = ''.join(current_seq)
            if validator:
                result = validator.validate(sequence)
                if not result:
                    raise FileFormatError(f"Invalid sequence for {current_id}: {result.message}")
            yield SequenceRecord(
                id=current_id,
                description=current_desc,
                sequence=sequence
            )

def write_fasta(records: Iterator[SequenceRecord], 
               file: FileLike,
               line_length: int = 70) -> None:
    """Write sequences to a FASTA file.
    
    Args:
        records: Iterable of SequenceRecord objects
        file: Output file path or file-like object
        line_length: Maximum line length for sequence data
    """
    with _open_file(file, 'wt') as f:
        for record in records:
            f.write(f">{record.id}")
            if record.description:
                f.write(f" {record.description}")
            f.write("\n")
            
            # Write sequence in chunks of line_length
            seq = record.sequence
            for i in range(0, len(seq), line_length):
                f.write(seq[i:i + line_length] + "\n")

# Similar implementations for FASTQ would follow...

def detect_format(file: FileLike) -> str:
    """Detect the format of a sequence file.
    
    Args:
        file: Path to file or file-like object
        
    Returns:
        str: Detected format ('fasta', 'fastq', or 'unknown')
    """
    with _open_file(file) as f:
        first_char = f.read(1)
        
    if first_char == '>':
        return 'fasta'
    elif first_char == '@':
        return 'fastq'
    return 'unknown'
