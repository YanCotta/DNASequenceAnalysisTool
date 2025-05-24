# 🧬 DNA Sequence Analysis Tool

A high-performance Python library and command-line tool for comprehensive DNA/RNA sequence analysis with advanced visualization capabilities.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Documentation](https://img.shields.io/badge/Documentation-Read%20the%20Docs-blue)](https://dna-sequence-analysis-tool.readthedocs.io/)
[![Tests](https://github.com/YanCotta/DNASequenceAnalysisTool/actions/workflows/tests.yml/badge.svg)](https://github.com/YanCotta/DNASequenceAnalysisTool/actions)
[![Codecov](https://codecov.io/gh/YanCotta/DNASequenceAnalysisTool/branch/main/graph/badge.svg)](https://codecov.io/gh/YanCotta/DNASequenceAnalysisTool)

A comprehensive Python toolkit for DNA sequence analysis, manipulation, and visualization.

---

## 📑 Table of Contents

- [Key Features](#-key-features)
- [Project Structure](#-project-structure)
- [Requirements](#-requirements)
- [Installation](#-quick-installation)
- [Quick Start](#-quick-start)
- [API Documentation](#-api-documentation)
- [Component Details](#-component-details)
- [Usage Examples](#-usage-examples)
- [Configuration](#-configuration)
- [Testing](#-testing)
- [Contributing](#-contributing)
- [Performance](#-performance)
- [License](#-license)
- [Contact & Support](#-contact--support)
- [Changelog](#-changelog)

---

## 🌟 Features

### Sequence Analysis

- GC content calculation
- Melting temperature prediction
- ORF detection and analysis
- Nucleotide composition analysis
- Pattern recognition and motif finding

### Molecular Biology Tools

- DNA/RNA transcription
- Codon-optimized protein translation
- Sophisticated ORF detection
- Advanced melting temperature calculations

### File I/O Support

- FASTA/FASTQ format support
- GZIP/BZIP2 compression
- Batch processing capabilities
- Format conversion utilities

### Visualization

- GC content plots
- Sequence logos
- Multiple sequence alignments
- Interactive visualizations

### Command Line Interface

- Intuitive command structure
- Batch processing support
- Multiple output formats (text, JSON, CSV)
- Visualization export to image files

---

## 🏗️ Project Structure

```text
dna_sequence_analysis_tool/
├── core/
│   ├── __init__.py
│   ├── sequence_analysis.py
│   ├── sequence_validation.py
│   └── visualization.py
├── data/
│   └── sample_sequences.fasta
├── utils/
│   ├── file_io.py
│   └── logging.py
├── tests/
│   ├── test_sequence_analysis.py
│   └── test_validation.py
├── cli.py
├── README.md
└── requirements.txt
```

## 📋 Requirements

- Python 3.8+

### Core Dependencies

- NumPy >= 1.19.0
- SciPy >= 1.5.0
- Biopython >= 1.78
- pandas >= 1.2.0
- matplotlib >= 3.3.0 (for visualization)
- click >= 8.0.0 (for CLI)
- rich >= 10.0.0 (for rich CLI output)
- plotly >= 5.0.0 (for interactive visualizations)

### Optional Dependencies

- python-magic (for file type detection)
- python-magic-bin (Windows only, for file type detection)

## 📦 Installation

```bash
# Install from PyPI
pip install dna-sequence-analysis-tool

# Install from source
git clone https://github.com/YanCotta/DNASequenceAnalysisTool.git
cd DNASequenceAnalysisTool
pip install -e .
```

---

## 🔍 Quick Start

```python
from dna_sequence_analysis_tool import DNAToolkit

# Initialize toolkit
toolkit = DNAToolkit()

# Analyze a sequence
sequence = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"
result = toolkit.analyze_sequence(sequence)
print(f"GC Content: {result.gc_content}%")
```

---

## 📊 API Documentation

### Core Classes

#### DNASequence

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

#### validate_sequence(sequence)

- Validates DNA sequences (A, T, G, C)
- Returns: (bool, str) - validity status and error message

#### calculate_gc_content(dna_sequence)

- Calculates GC content percentage
- Raises ValueError for invalid sequences

#### reverse_complement(dna_sequence)

- Generates reverse complement of DNA sequence
- Returns: String of complementary sequence

#### find_motif(dna_sequence, motif)

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
- Sequence manipulation and transformation methods

#### `sequence_analysis.py`
- Advanced sequence analysis algorithms
- ORF detection and promoter prediction
- Local and global sequence alignment
- Repeat sequence analysis
- Motif finding and pattern matching

#### `sequence_io.py`
- Reading and writing FASTA/FASTQ files
- Support for gzip and bzip2 compression
- Automatic format detection
- Sequence validation during I/O operations

#### `sequence_validation.py`
- Sequence validation for DNA/RNA
- Support for ambiguous bases
- Configurable validation rules
- Detailed error reporting

#### `visualization.py`
- GC content plots
- Sequence logos
- Multiple sequence alignment visualization
- Interactive plots with Plotly
- Export to various image formats

#### `sequence_statistics.py`
- Sequence complexity measures
- Nucleotide frequency analysis
- Statistical significance calculations
- Sequence similarity metrics

### Command Line Interface (`cli.py`)
- Interactive command-line interface
- Support for batch processing
- Rich text formatting and progress bars
- Multiple output formats (text, JSON, CSV)
- Integrated help system

## 📊 Visualization Examples

### GC Content Plot

```python
from dna_sequence_analysis_tool.visualization import plot_gc_content

sequence = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"
fig = plot_gc_content(sequence, window_size=10, step_size=1)
fig.savefig("gc_content.png")
```

### Sequence Logo

```python
from dna_sequence_analysis_tool.visualization import plot_sequence_logo

sequences = ["ATCG", "ATTA", "ATGC", "ATAA"]
fig = plot_sequence_logo(sequences)
fig.savefig("sequence_logo.png")
```

### Multiple Sequence Alignment

```python
from dna_sequence_analysis_tool.visualization import plot_alignment

alignment = [
    "ATCGATCGAT",
    "AT-GATCGAT",
    "ATCGAT---T",
    "ATCGATCGAT"
]

fig = plot_alignment(alignment, title="Multiple Sequence Alignment")
fig.savefig("alignment.png")
```

## 🛠️ Command Line Interface

The DNA Sequence Analysis Tool comes with a powerful command-line interface for batch processing and automation:

### Basic Usage

```bash
# Analyze a single sequence file
dna-tool analyze sequences.fasta --output results.json

# Process multiple files in a directory
dna-tool batch-process input_dir/ --output results/

# Convert between file formats
dna-tool convert input.fasta --output output.fastq --format fastq
```

### Available Commands

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

## 📊 Performance

### Performance Metrics

| Operation           | Time Complexity | Space Complexity |
|:-------------------|:---------------:|:----------------:|
| Sequence Validation | O(n)             | O(1)             |
| GC Content          | O(n)             | O(1)             |
| ORF Detection       | O(n)             | O(n)             |
| Sequence Alignment  | O(mn)            | O(mn)            |


---

---

## 🌟 Support This Project

If you find this tool useful, please consider giving it a ⭐ on [GitHub](https://github.com/YanCotta/DNASequenceAnalysisTool)

Made with ❤️ for the bioinformatics community

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

# Changelog

## 📝 Changelog

### [Unreleased]

- Added command-line interface with rich output
- Enhanced visualization capabilities (GC content, sequence logos, alignments)
- Improved sequence I/O with gzip/bzip2 compression support
- Added comprehensive documentation and examples
- Added support for batch processing of sequence files
- Implemented multiple output formats (text, JSON, CSV)

### [0.2.0] - 2023-06-15

- Added sequence visualization module with matplotlib and plotly support
- Implemented FASTA/FASTQ file format support
- Added sequence validation framework with configurable rules
- Improved error handling and logging
- Added support for ambiguous nucleotide codes

### [0.1.0] - 2023-01-01

- Initial release with core DNA/RNA analysis functionality
- Basic sequence manipulation and analysis tools
- Comprehensive documentation and examples usage
- Optimized sequence processing

---

## DNA Sequence Analysis Tool v2.8 (Latest)
### Added
- Graceful fallback for operations when NumPy/SciPy are not available
- Enhanced error handling and validation across all modules
- Memory-efficient sequence processing with caching
- Improved logging system with configurable output
- Added molecular weight calculations
- Added sequence complexity analysis
- Implemented affine gap penalties in sequence alignment

### Changed
- Optimized GC content calculation
- Improved TATA box prediction algorithm
- Enhanced repeat sequence detection
- Better integration between basic and advanced analyzers
- More robust sequence validation
- Updated dependencies to latest stable versions

### Fixed
- Fixed dependency management in setup.py and requirements.txt
- Resolved numpy/scipy import issues
- Improved error messages and exception handling
- Fixed memory leaks in sequence analysis
- Corrected molecular weight calculations

### Technical Improvements
- Added type hints throughout the codebase
- Improved test coverage
- Better documentation and code organization
- Memory optimizations for large sequences
- Performance improvements in core algorithms

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