"""
Basic sequence analysis example.

This script demonstrates basic sequence analysis using the DNA Sequence Analysis Tool.
"""
from dna_sequence_analysis_tool import DNASequence, DNAToolkit
from dna_sequence_analysis_tool.logging_config import get_logger

# Set up logging
logger = get_logger(__name__)

def main():
    """Run basic sequence analysis example."""
    # Initialize toolkit
    toolkit = DNAToolkit()
    
    # Example sequence
    sequence = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"
    
    try:
        # Create a DNA sequence object
        dna_seq = DNASequence(sequence, "example_sequence")
        
        # Print sequence info
        logger.info(f"Sequence ID: {dna_seq.id}")
        logger.info(f"Sequence length: {dna_seq.length} bp")
        logger.info(f"GC content: {dna_seq.gc_content:.2f}%")
        
        # Get reverse complement
        rev_comp = dna_seq.reverse_complement()
        logger.info(f"Reverse complement: {rev_comp}")
        
        # Find motifs
        motif = "GGC"
        positions = dna_seq.find_motif(motif)
        logger.info(f"Motif '{motif}' found at positions: {positions}")
        
        # Calculate melting temperature
        tm = toolkit.calculate_melting_temperature(dna_seq.sequence)
        logger.info(f"Melting temperature: {tm:.2f}°C")
        
    except Exception as e:
        logger.error(f"Error during sequence analysis: {e}", exc_info=True)
        raise

if __name__ == "__main__":
    main()
