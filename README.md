## DNA Sequence Analysis Tool
This repository contains a Python script for analyzing DNA sequences. The script provides several functions to validate DNA sequences, calculate GC content, find motifs, and generate reverse complements. This tool is useful for bioinformatics and computational biology applications.

## Features
- Validate DNA Sequence: Ensures the sequence contains only valid DNA nucleotides (A, T, G, C).
- Calculate GC Content: Computes the percentage of guanine (G) and cytosine (C) in the DNA sequence.
- Reverse Complement: Generates the reverse complement of a DNA sequence.
- Find Motif: Searches for all occurrences of a motif within a DNA sequence.
- Sequence Statistics: Provides various statistics about the DNA sequence, including length, GC content, and nucleotide counts.

## Usage
### Prerequisites
- Python 3.x
### Running the Script
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/dna-sequence-analysis-tool.git
    cd dna-sequence-analysis-tool
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

## Functions
 `validate_sequence(sequence) > Validates if the sequence contains only valid DNA nucleotides (A, T, G, C).`

 `calculate_gc_content(dna_sequence)` > Calculates the percentage of G and C in the DNA sequence.

 `reverse_complement(dna_sequence)` > Returns the reverse complement of the DNA sequence.

 `find_motif(dna_sequence, motif)` > Searches for all occurrences of the motif in the DNA sequence.

 `sequence_statistics(dna_sequence)` > Returns a dictionary containing various statistics about the DNA sequence.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any questions or inquiries, please contact yanpcotta@gmail.com

---

This project showcases the intersection of biology and data science, demonstrating skills in bioinformatics and computational biology.