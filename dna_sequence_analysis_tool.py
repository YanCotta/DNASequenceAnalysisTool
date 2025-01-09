def validate_sequence(sequence):
    """
    Validates if the sequence contains only valid DNA nucleotides (A, T, G, C).
    Returns tuple (bool, str) indicating validity and error message if invalid.
    """
    valid_nucleotides = set('ATGC')
    sequence = sequence.upper()
    invalid_chars = set(sequence) - valid_nucleotides
    if invalid_chars:
        return False, f"Invalid nucleotides found: {', '.join(invalid_chars)}"
    return True, ""

def calculate_gc_content(dna_sequence):
    """
    Calculates the percentage of G and C in the DNA sequence.
    Raises ValueError if sequence is invalid.
    """
    is_valid, error_msg = validate_sequence(dna_sequence)
    if not is_valid:
        raise ValueError(error_msg)
    
    dna_sequence = dna_sequence.upper()
    gc_count = dna_sequence.count('G') + dna_sequence.count('C')
    return (gc_count / len(dna_sequence)) * 100 if dna_sequence else 0

def reverse_complement(dna_sequence):
    """
    Returns the reverse complement of the DNA sequence.
    Raises ValueError if sequence is invalid.
    """
    is_valid, error_msg = validate_sequence(dna_sequence)
    if not is_valid:
        raise ValueError(error_msg)
        
    complement_map = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    return ''.join(complement_map[base] for base in dna_sequence.upper()[::-1])

def find_motif(dna_sequence, motif):
    """
    Searches for all occurrences of the motif in the DNA sequence.
    Returns a list of starting indices (0-based).
    Raises ValueError if either sequence is invalid.
    """
    for seq in [dna_sequence, motif]:
        is_valid, error_msg = validate_sequence(seq)
        if not is_valid:
            raise ValueError(error_msg)
    
    dna_sequence = dna_sequence.upper()
    motif = motif.upper()
    positions = []
    for i in range(len(dna_sequence) - len(motif) + 1):
        if dna_sequence[i:i+len(motif)] == motif:
            positions.append(i)
    return positions

def sequence_statistics(dna_sequence):
    """
    Returns a dictionary containing various statistics about the DNA sequence.
    """
    is_valid, error_msg = validate_sequence(dna_sequence)
    if not is_valid:
        raise ValueError(error_msg)
        
    sequence = dna_sequence.upper()
    return {
        'length': len(sequence),
        'gc_content': calculate_gc_content(sequence),
        'nucleotide_counts': {
            'A': sequence.count('A'),
            'T': sequence.count('T'),
            'G': sequence.count('G'),
            'C': sequence.count('C')
        }
    }

def main():
    """
    Demonstrates the DNA sequence analysis tools with error handling.
    """
    try:
        # Example usage with a sample DNA sequence
        sample_dna = "AGCTATCGGCTAGCG"
        motif = "CG"
        
        print("\nDNA Sequence Analysis Results")
        print("-" * 30)
        print(f"Sequence: {sample_dna}")
        
        # Get and display sequence statistics
        stats = sequence_statistics(sample_dna)
        print(f"\nSequence Statistics:")
        print(f"Length: {stats['length']}")
        print(f"GC Content: {stats['gc_content']:.2f}%")
        print("Nucleotide Counts:")
        for base, count in stats['nucleotide_counts'].items():
            print(f"  {base}: {count}")
        
        # Display reverse complement
        print(f"\nReverse Complement: {reverse_complement(sample_dna)}")
        
        # Find and display motif positions
        positions = find_motif(sample_dna, motif)
        print(f"\nMotif '{motif}' found at positions: {positions}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
