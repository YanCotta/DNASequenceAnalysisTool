# DNA Sequence Analysis Tool 🧬

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Tests](https://github.com/yourusername/DNASequenceAnalysisTool/workflows/Tests/badge.svg)](https://github.com/yourusername/DNASequenceAnalysisTool/actions)

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
git clone https://github.com/yourusername/DNASequenceAnalysisTool.git
cd DNASequenceAnalysisTool
pip install -e .
```

## 🎯 Quick Start

```python
from dna_analysis import DNASequence

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

## 📦 Performance

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Sequence Validation | O(n) | O(1) |
| GC Content | O(n) | O(1) |
| ORF Detection | O(n) | O(n) |
| Sequence Alignment | O(mn) | O(mn) |

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

## 📫 Contact & Support

- **Author**: Yan Cotta
- **Email**: yanpcotta@gmail.com
- **Issues**: [GitHub Issues](https://github.com/YanCotta/DNASequenceAnalysisTool/issues)

## 🌟 Acknowledgments

- BioPython community
- Python Bioinformatics Working Group
- Our fantastic contributors

---

<div align="center">
Made with ❤️ for the bioinformatics community
</div>

# Changelog

## DNA Sequence Analysis Tool v2.0
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