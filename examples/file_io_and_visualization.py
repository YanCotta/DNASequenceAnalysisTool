"""
File I/O and visualization example.

This script demonstrates reading sequences from a file, analyzing them,
and creating visualizations using the DNA Sequence Analysis Tool.
"""
import os
import matplotlib.pyplot as plt
from pathlib import Path

from dna_sequence_analysis_tool import DNASequence, DNAToolkit
from dna_sequence_analysis_tool.logging_config import get_logger

# Set up logging
logger = get_logger(__name__)

def analyze_sequences(input_file: str, output_dir: str = "output"):
    """
    Analyze sequences from a file and generate visualizations.
    
    Args:
        input_file: Path to input FASTA/FASTQ file
        output_dir: Directory to save output files
    """
    # Create output directory if it doesn't exist
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    # Initialize toolkit
    toolkit = DNAToolkit()
    
    try:
        # Read sequences from file
        logger.info(f"Reading sequences from {input_file}")
        sequences = toolkit.read_sequences(input_file)
        logger.info(f"Found {len(sequences)} sequences")
        
        # Analyze each sequence
        gc_contents = []
        sequence_lengths = []
        
        for seq in sequences:
            # Basic analysis
            gc_contents.append(seq.gc_content)
            sequence_lengths.append(seq.length)
            
            # Find ORFs
            orfs = toolkit.find_orfs(seq.sequence)
            logger.info(f"Found {len(orfs)} ORFs in sequence {seq.id}")
        
        # Generate GC content plot
        plt.figure(figsize=(10, 6))
        plt.hist(gc_contents, bins=20, alpha=0.7, color='skyblue')
        plt.title('GC Content Distribution')
        plt.xlabel('GC Content (%)')
        plt.ylabel('Frequency')
        plt.grid(True, linestyle='--', alpha=0.7)
        gc_plot_path = output_path / 'gc_content_distribution.png'
        plt.savefig(gc_plot_path, dpi=300, bbox_inches='tight')
        logger.info(f"Saved GC content plot to {gc_plot_path}")
        
        # Generate sequence length plot
        plt.figure(figsize=(10, 6))
        plt.hist(sequence_lengths, bins=20, alpha=0.7, color='lightgreen')
        plt.title('Sequence Length Distribution')
        plt.xlabel('Sequence Length (bp)')
        plt.ylabel('Frequency')
        plt.grid(True, linestyle='--', alpha=0.7)
        len_plot_path = output_path / 'sequence_length_distribution.png'
        plt.savefig(len_plot_path, dpi=300, bbox_inches='tight')
        logger.info(f"Saved sequence length plot to {len_plot_path}")
        
        # Save analysis summary
        summary_path = output_path / 'analysis_summary.txt'
        with open(summary_path, 'w') as f:
            f.write("Sequence Analysis Summary\n")
            f.write("========================\n\n")
            f.write(f"Input file: {input_file}\n")
            f.write(f"Number of sequences: {len(sequences)}\n")
            f.write(f"Average GC content: {sum(gc_contents)/len(gc_contents):.2f}%\n")
            f.write(f"Average sequence length: {sum(sequence_lengths)/len(sequence_lengths):.2f} bp\n")
            
        logger.info(f"Analysis complete. Summary saved to {summary_path}")
        
    except Exception as e:
        logger.error(f"Error during sequence analysis: {e}", exc_info=True)
        raise

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Analyze DNA sequences from a file')
    parser.add_argument('input_file', help='Input FASTA/FASTQ file')
    parser.add_argument('-o', '--output-dir', default='output', help='Output directory')
    
    args = parser.parse_args()
    
    analyze_sequences(args.input_file, args.output_dir)
