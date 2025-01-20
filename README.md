# DNA Sequence Analysis Tool 🧬

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A high-performance Python library for comprehensive DNA sequence analysis, providing industrial-grade molecular biology and bioinformatics capabilities.

## 🚀 Key Features

- **Sequence Validation & Analysis**
  - Robust DNA/RNA sequence validation
  - Advanced GC content analysis
  - Comprehensive nucleotide statistics
  - Pattern recognition and motif finding

- **Molecular Biology Tools**
  - DNA ↔ RNA transcription
  - Codon-optimized protein translation
  - Sophisticated ORF detection
  - Advanced melting temperature calculations

- **Bioinformatics Capabilities**
  - Local sequence alignment
  - Global sequence alignment scoring
  - Enhanced sequence metrics
  - Performance-optimized algorithms

## 📁 Project Structure

```
dna_sequence_analysis_tool/
├── core/                     # Core analysis functionality
│   ├── __init__.py
│   ├── main.py              # Main interface and toolkit
│   ├── sequence_analysis.py  # Advanced analysis algorithms
│   ├── sequence_statistics.py# Statistical calculations
│   ├── sequence_transformation.py # DNA/RNA transformations
│   └── sequence_validation.py# Sequence validation utilities
├── data/                    # Data handling and sample sequences
│   ├── __init__.py
│   └── sample_sequence.py   # Pre-defined test sequences
├── utils/                   # Utility functions
│   ├── __init__.py
│   ├── file_io.py          # FASTA file handling
│   └── logging.py          # Logging configuration
└── tests/                   # Test suite (coming in v3.0)
```

## 📋 Requirements

- Python 3.6+
- NumPy >= 1.19.0
- Biopython >= 1.78
- pandas >= 1.2.0

## ⚡️ Quick Installation

```bash
# Via pip
pip install dna-sequence-analysis

# Via conda
conda install -c bioconda dna-sequence-analysis

# Development installation
git clone https://github.com/YanCotta/DNASequenceAnalysisTool.git
cd DNASequenceAnalysisTool
pip install -e .
```

## 🎯 Quick Start

```python
from dna_sequence_analysis_tool import DNASequence

# Initialize with your sequence
seq = DNASequence("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")

# Basic analysis
print(f"GC Content: {seq.gc_content:.2f}%")
print(f"Molecular Weight: {seq.molecular_weight:.2f} Da")
print(f"Melting Temperature: {seq.melting_temp:.1f}°C")

# Advanced features
orfs = seq.find_orfs(min_length=30)
proteins = seq.translate()
alignments = seq.align_with("ATGGCCATTGTAATG")
```

## 📘 API Documentation

### Core Classes

#### `DNASequence`
```python
class DNASequence:
    """
    Core class for DNA sequence analysis.
    
    Attributes:
        sequence (str): The DNA sequence
        length (int): Sequence length
        gc_content (float): GC content percentage
    """
```

### Basic Functions

#### `validate_sequence(sequence)`
- Validates DNA sequences (A, T, G, C)
- Returns: (bool, str) - validity status and error message

#### `calculate_gc_content(dna_sequence)`
- Calculates GC content percentage
- Raises ValueError for invalid sequences

#### `reverse_complement(dna_sequence)`
- Generates reverse complement of DNA sequence
- Returns: String of complementary sequence

#### `find_motif(dna_sequence, motif)`
- Finds all occurrences of a motif
- Returns: List of starting positions (0-based)

### Advanced Functions

#### `validate_rna_sequence(sequence)`
- Validates RNA sequences (A, U, G, C)
- Returns: (bool, str) - validity status and error message

#### `transcribe(dna_sequence)`
- Converts DNA to RNA sequence
- Returns: RNA sequence (replaces T with U)

#### `translate(rna_sequence)`
- Converts RNA to protein sequence
- Returns: Amino acid sequence using standard genetic code

#### `find_orfs(dna_sequence, min_length=30)`
- Finds all possible Open Reading Frames
- Parameters:
  - min_length: Minimum ORF length (default: 30)
- Returns: List of (start_position, sequence, frame)

#### `calculate_melting_temp(dna_sequence)`
- Calculates DNA melting temperature
- Uses different formulas based on sequence length:
  - < 14 bases: Tm = (A+T)*2 + (G+C)*4
  - ≥ 14 bases: Tm = 64.9 + 41*(G+C-16.4)/(A+T+G+C)

#### `sequence_alignment_score(seq1, seq2)`
- Calculates similarity between two sequences
- Returns: Percentage of matching positions

#### `enhanced_sequence_statistics(dna_sequence)`
- Provides comprehensive sequence analysis including:
  - Basic statistics (length, GC content, nucleotide counts)
  - Dinucleotide frequencies
  - Melting temperature
  - Molecular weight

## 🔬 Component Details

### Core Package (`core/`)

#### `main.py`
- `DNAToolkit` class: Primary interface for DNA analysis
- Comprehensive sequence analysis pipeline
- Integrated logging and error handling

#### `sequence_analysis.py`
- Advanced sequence analysis algorithms
- ORF detection and promoter prediction
- Local and global sequence alignment
- Repeat sequence analysis

#### `sequence_statistics.py`
- GC content calculation
- Melting temperature analysis
- Nucleotide frequency statistics
- Parallel processing for large sequences

#### `sequence_transformation.py`
- DNA/RNA transcription
- Protein translation
- Sequence complementation
- Codon optimization

#### `sequence_validation.py`
- Robust sequence validation
- Multiple sequence format support
- IUPAC nucleotide validation
- Reading frame validation

### Data Package (`data/`)

#### `sample_sequence.py`
- Pre-defined test sequences
- Common genetic elements
- FASTA file loading
- Sequence validation integration

### Utils Package (`utils/`)

#### `file_io.py`
- FASTA file reading/writing
- Sequence format conversion
- Error handling and logging
- File validation

#### `logging.py`
- Centralized logging configuration
- Debug and error tracking
- Operation monitoring
- Performance logging

## 🎯 Usage Examples

### Basic Sequence Analysis
```python
from dna_sequence_analysis_tool import DNAToolkit

# Initialize toolkit
toolkit = DNAToolkit()

# Analyze sequence
sequence = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"
results = toolkit.analyze_sequence(sequence)

# Access results
print(f"GC Content: {results.gc_content}%")
print(f"Molecular Weight: {results.molecular_weight}")
```

### File Operations
```python
from dna_sequence_analysis_tool.utils.file_io import read_fasta, write_fasta

# Read sequences from FASTA
sequences = read_fasta("sequences.fasta")

# Process and write results
write_fasta(sequences, "processed_sequences.fasta")
```

### Advanced Analysis
```python
from dna_sequence_analysis_tool.core.sequence_analysis import AdvancedSequenceAnalyzer

# Initialize analyzer
analyzer = AdvancedSequenceAnalyzer()

# Predict promoter regions
promoters = analyzer.predict_promoter_regions(sequence)

# Analyze repeats
repeats = analyzer.analyze_repeats(sequence)
```

## 🔧 Configuration

### Logging Configuration
```python
from dna_sequence_analysis_tool.utils.logging import logger

# Set custom log level
logger.setLevel(logging.DEBUG)

# Add custom handler
handler = logging.FileHandler('analysis.log')
logger.addHandler(handler)
```

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=dna_analysis tests/
```

## 🤝 Contributing

We welcome contributions! 

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📊 Performance Optimizations

- Cached sequence validation
- Parallel processing for large sequences
- Memory-efficient data structures
- Optimized algorithms for common operations

## 📦 Performance

| Operation           | Time Complexity | Space Complexity |
|---------------------|------------------|------------------|
| Sequence Validation | O(n)             | O(1)             |
| GC Content          | O(n)             | O(1)             |
| ORF Detection       | O(n)             | O(n)             |
| Sequence Alignment  | O(mn)            | O(mn)            |

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

## 📫 Contact & Support

- **Author**: Yan Cotta
- **Email**: yanpcotta@gmail.com
- **Issues**: [GitHub Issues](https://github.com/YanCotta/DNASequenceAnalysisTool/issues)

---

<div align="center">
Made with ❤️ for the bioinformatics community
</div>

# Changelog

## DNA Sequence Analysis Tool v2.7
### Added
- Advanced ORF detection system
- Enhanced melting temperature calculations
- Sequence alignment scoring
- Comprehensive sequence statistics
- RNA sequence validation
- Protein translation features
- Type hints for all functions

### Changed
- Improved documentation
- Enhanced error handling
- Updated example usage
- Optimized sequence processing

## DNA Sequence Analysis Tool v3.0 (Future Release)
### Planned
#### Testing:
- Add more comprehensive unit tests
- Include integration tests
- Add test coverage reporting
- Test edge cases and biological validity

#### Biological Features:
- Implement codon usage bias analysis
- Add protein structure prediction
- Include phylogenetic analysis capabilities
- Add primer design functionality

#### Performance:
- Implement parallel processing for large sequences
- Add memory optimization for large datasets
- Include progress tracking for long operations
- Add visualization capabilities
- Implement machine learning for sequence analysis
- Add web interface

#### Documentation:
- Add biological background for each analysis
- Include example workflows
- Add benchmarking results
- Document algorithm complexity
- Updated outdated README to properly reference the project and its functionalities 

#### Code Quality: 
- Add type hints consistently
- Improve error messages
- Add performance metrics
- Implement logging