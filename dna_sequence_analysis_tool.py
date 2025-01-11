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

def validate_rna_sequence(sequence):
    """
    Validates if the sequence contains only valid RNA nucleotides (A, U, G, C).
    Returns tuple (bool, str) indicating validity and error message if invalid.
    """
    valid_nucleotides = set('AUGC')
    sequence = sequence.upper()
    invalid_chars = set(sequence) - valid_nucleotides
    if invalid_chars:
        return False, f"Invalid RNA nucleotides found: {', '.join(invalid_chars)}"
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

def transcribe(dna_sequence):
    """
    Transcribes DNA to RNA (replaces T with U).
    Raises ValueError if sequence is invalid.
    """
    is_valid, error_msg = validate_sequence(dna_sequence)
    if not is_valid:
        raise ValueError(error_msg)
    return dna_sequence.upper().replace('T', 'U')

def translate(rna_sequence):
    """
    Translates RNA sequence to protein sequence using the standard genetic code.
    Returns the protein sequence as a string.
    """
    is_valid, error_msg = validate_rna_sequence(rna_sequence)
    if not is_valid:
        raise ValueError(error_msg)
    
    genetic_code = {
        'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L', 'CUU': 'L', 'CUC': 'L',
        'CUA': 'L', 'CUG': 'L', 'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V', 'UCU': 'S', 'UCC': 'S',
        'UCA': 'S', 'UCG': 'S', 'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'GCU': 'A', 'GCC': 'A',
        'GCA': 'A', 'GCG': 'A', 'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',
        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'AAU': 'N', 'AAC': 'N',
        'AAA': 'K', 'AAG': 'K', 'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W', 'CGU': 'R', 'CGC': 'R',
        'CGA': 'R', 'CGG': 'R', 'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }
    
    protein = []
    for i in range(0, len(rna_sequence)-2, 3):
        codon = rna_sequence[i:i+3]
        if len(codon) == 3:
            amino_acid = genetic_code.get(codon, 'X')
            if amino_acid == '*':  # Stop codon
                break
            protein.append(amino_acid)
    
    return ''.join(protein)

def find_orfs(dna_sequence, min_length=30):
    """
    Finds all possible Open Reading Frames (ORFs) in the DNA sequence.
    Returns a list of tuples (start_position, sequence, frame).
    min_length: minimum length of ORF in nucleotides
    """
    is_valid, error_msg = validate_sequence(dna_sequence)
    if not is_valid:
        raise ValueError(error_msg)
    
    start_codon = 'ATG'
    stop_codons = ['TAA', 'TAG', 'TGA']
    orfs = []
    
    sequence = dna_sequence.upper()
    # Check all three reading frames
    for frame in range(3):
        for i in range(frame, len(sequence)-2, 3):
            if sequence[i:i+3] == start_codon:
                # Found start codon, look for stop codon
                for j in range(i+3, len(sequence)-2, 3):
                    if sequence[j:j+3] in stop_codons:
                        if j-i >= min_length:
                            orfs.append((i, sequence[i:j+3], frame+1))
                        break
    return orfs

def calculate_melting_temp(dna_sequence):
    """
    Calculates the melting temperature of DNA sequence using the nearest-neighbor method.
    This is a simplified version using the basic formula for sequences < 14 bases:
    Tm = (A+T)*2 + (G+C)*4
    
    For sequences ≥ 14 bases, uses the formula:
    Tm = 64.9 + 41*(G+C-16.4)/(A+T+G+C)
    """
    is_valid, error_msg = validate_sequence(dna_sequence)
    if not is_valid:
        raise ValueError(error_msg)
        
    sequence = dna_sequence.upper()
    a_count = sequence.count('A')
    t_count = sequence.count('T')
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    
    if len(sequence) < 14:
        return (a_count + t_count) * 2 + (g_count + c_count) * 4
    else:
        gc_content = (g_count + c_count) / len(sequence)
        return 64.9 + 41 * (gc_content - 16.4) / len(sequence)

def sequence_alignment_score(seq1, seq2):
    """
    Performs a simple sequence alignment using Hamming distance.
    Returns the similarity score (percentage of matching positions).
    Sequences must be of equal length.
    """
    if len(seq1) != len(seq2):
        raise ValueError("Sequences must be of equal length for simple alignment")
    
    for seq in [seq1, seq2]:
        is_valid, error_msg = validate_sequence(seq)
        if not is_valid:
            raise ValueError(error_msg)
    
    matches = sum(1 for a, b in zip(seq1.upper(), seq2.upper()) if a == b)
    return (matches / len(seq1)) * 100

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

def enhanced_sequence_statistics(dna_sequence):
    """
    Returns an enhanced dictionary containing various statistics about the DNA sequence.
    """
    basic_stats = sequence_statistics(dna_sequence)
    
    # Add more advanced statistics
    sequence = dna_sequence.upper()
    dinucleotides = {}
    for i in range(len(sequence)-1):
        pair = sequence[i:i+2]
        dinucleotides[pair] = dinucleotides.get(pair, 0) + 1
    
    return {
        **basic_stats,
        'dinucleotide_counts': dinucleotides,
        'melting_temperature': calculate_melting_temp(sequence),
        'molecular_weight': sum(
            {'A': 313.21, 'T': 304.2, 'G': 329.21, 'C': 289.18}[base] 
            for base in sequence
        ),
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
