# DNA Sequence Analysis Tool - Examples

This directory contains example scripts that demonstrate how to use the DNA Sequence Analysis Tool.

## Available Examples

### 1. Basic Sequence Analysis

**File:** `basic_sequence_analysis.py`

This example demonstrates basic sequence analysis functionality, including:
- Creating a DNA sequence object
- Calculating GC content
- Finding reverse complement
- Finding motifs
- Calculating melting temperature

**How to run:**
```bash
python examples/basic_sequence_analysis.py
```

### 2. File I/O and Visualization

**File:** `file_io_and_visualization.py`

This example shows how to:
- Read sequences from a FASTA/FASTQ file
- Perform basic sequence analysis
- Generate visualizations (GC content, sequence length distribution)
- Save analysis results

**How to run:**
```bash
# Basic usage
python examples/file_io_and_visualization.py path/to/your/sequences.fasta

# With custom output directory
python examples/file_io_and_visualization.py path/to/your/sequences.fasta -o my_output_dir
```

## Sample Data

To test the examples, you can use the sample FASTA file provided in the `data` directory or use your own sequence files.

## Requirements

All examples require the DNA Sequence Analysis Tool and its dependencies to be installed. Make sure to install the package in development mode:

```bash
pip install -e .
```

## Creating Your Own Examples

Feel free to use these examples as a starting point for your own scripts. The DNA Sequence Analysis Tool provides a rich set of features for sequence analysis, manipulation, and visualization.

For more information, refer to the [API Documentation](https://dna-sequence-analysis-tool.readthedocs.io/).
