# DNA Sequence Analysis Tool

A comprehensive Python tool for DNA sequence analysis that provides various molecular biology and bioinformatics functions.

## Features

### Basic DNA Analysis
- Sequence validation for DNA and RNA
- GC content calculation
- Reverse complement generation
- Motif finding

### Advanced Molecular Analysis
- DNA to RNA transcription
- RNA to protein translation
- Open Reading Frame (ORF) detection
- Melting temperature calculation
- Sequence alignment scoring
- Enhanced sequence statistics

## Usage
### Prerequisites
- Python 3.6 or higher

### Running the Script
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/DNASequenceAnalysisTool.git
    cd DNASequenceAnalysisTool
    ```

2. Run the script:
    ```sh
    python dna_sequence_analysis_tool.py
    ```

### Example Output
The script demonstrates its functionality using a sample DNA sequence. Below is an example of the output:

```
DNA Sequence Analysis Results
------------------------------
Sequence: AGCTATCGGCTAGCG

Sequence Statistics:
Length: 15
GC Content: 53.33%
Nucleotide Counts:
  A: 3
  T: 3
  G: 5
  C: 4

Reverse Complement: CGCTAGCCGATAGCT

Motif 'CG' found at positions: [5, 12]
```

## Function Documentation

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

## Usage Example

```python
# Basic DNA analysis
dna_sequence = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"
rna = transcribe(dna_sequence)
protein = translate(rna)

# Find ORFs
orfs = find_orfs(dna_sequence)

# Get comprehensive statistics
stats = enhanced_sequence_statistics(dna_sequence)

# Calculate melting temperature
tm = calculate_melting_temp(dna_sequence)

# Sequence alignment
similarity = sequence_alignment_score(seq1, seq2)
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any questions or inquiries, please contact yanpcotta@gmail.com

---

This project showcases the intersection of biology and data science, demonstrating skills in bioinformatics and computational biology.

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