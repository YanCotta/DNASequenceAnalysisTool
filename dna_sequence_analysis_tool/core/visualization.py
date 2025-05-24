"""
Sequence Visualization Module
=============================

This module provides functionality for visualizing DNA/RNA sequences,
alignments, and analysis results using matplotlib.

Features:
    - Sequence logos
    - Multiple sequence alignments
    - GC content plots
    - Restriction site visualization
    - Interactive plots with plotly (optional)

Example:
    >>> from dna_sequence_analysis_tool.core.visualization import plot_gc_content
    >>> plot_gc_content("ATGCGATCGATCGATCGATCG", window_size=5)
"""

from typing import List, Dict, Tuple, Optional, Union, Sequence
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Rectangle

# Try to import plotly for interactive visualizations
try:
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False

# Custom color schemes
NUCLEOTIDE_COLORS = {
    'A': '#109648',  # Green
    'T': '#F7B500',  # Yellow
    'G': '#FF6F00',  # Orange
    'C': '#1D4E89',  # Blue
    'U': '#F7B500',  # Same as T for RNA
    'N': '#CCCCCC',  # Gray for ambiguous
}

# Extend colors to IUPAC ambiguity codes
for nt, equiv in {
    'R': 'AG', 'Y': 'TC', 'S': 'GC', 'W': 'AT',
    'K': 'GT', 'M': 'AC', 'B': 'GTC', 'D': 'GAT',
    'H': 'ACT', 'V': 'GCA', 'N': 'GATCG'
}.items():
    # Average colors of the equivalent nucleotides
    colors = [NUCLEOTIDE_COLORS[n] for n in equiv]
    # Simple average of RGB values
    avg_color = f'#{int(sum(int(c[i:i+2], 16) for c in colors) / len(colors)):02x}'
    NUCLEOTIDE_COLORS[nt] = avg_color

def plot_sequence_logo(sequences: List[str], 
                      title: str = "Sequence Logo",
                      figsize: Tuple[int, int] = (12, 4),
                      color_scheme: Optional[Dict[str, str]] = None) -> plt.Figure:
    """Create a sequence logo from a list of aligned sequences.
    
    Args:
        sequences: List of aligned sequences (must be same length)
        title: Plot title
        figsize: Figure size (width, height)
        color_scheme: Custom color scheme for nucleotides
        
    Returns:
        matplotlib Figure object
    """
    if not sequences:
        raise ValueError("No sequences provided")
    
    seq_len = len(sequences[0])
    if any(len(seq) != seq_len for seq in sequences):
        raise ValueError("All sequences must be the same length")
    
    # Count nucleotide frequencies at each position
    counts = [{'A': 0, 'T': 0, 'G': 0, 'C': 0, 'N': 0} for _ in range(seq_len)]
    
    for seq in sequences:
        for i, nt in enumerate(seq.upper()):
            if nt in counts[i]:
                counts[i][nt] += 1
            else:
                counts[i]['N'] += 1
    
    # Convert counts to frequencies
    total = len(sequences)
    freqs = [{nt: c/total for nt, c in pos.items()} for pos in counts]
    
    # Create figure
    fig, ax = plt.subplots(figsize=figsize)
    
    # Use custom colors if provided, otherwise use defaults
    colors = color_scheme or NUCLEOTIDE_COLORS
    
    # Plot each position
    for pos in range(seq_len):
        # Sort nucleotides by frequency for this position
        sorted_nts = sorted(freqs[pos].items(), key=lambda x: x[1], reverse=True)
        
        # Plot each nucleotide stack
        height_so_far = 0
        for nt, freq in sorted_nts:
            if freq > 0:
                ax.add_patch(Rectangle(
                    (pos, height_so_far), 1, freq,
                    facecolor=colors.get(nt, '#CCCCCC'),
                    edgecolor='white',
                    linewidth=0.5
                ))
                
                # Add nucleotide letter
                if freq > 0.05:  # Only show letter if big enough
                    ax.text(
                        pos + 0.5, height_so_far + freq/2,
                        nt,
                        ha='center', va='center',
                        color='white' if colors.get(nt, '#000000').lower() != '#ffffff' else 'black',
                        fontweight='bold',
                        fontsize=10
                    )
                
                height_so_far += freq
    
    # Customize plot
    ax.set_xlim(0, seq_len)
    ax.set_ylim(0, 1)
    ax.set_xticks(range(seq_len))
    ax.set_xticklabels(range(1, seq_len + 1))
    ax.set_xlabel("Position")
    ax.set_ylabel("Frequency")
    ax.set_title(title)
    
    plt.tight_layout()
    return fig

def plot_gc_content(sequence: str, 
                   window_size: int = 100,
                   step_size: int = 10,
                   title: str = "GC Content") -> plt.Figure:
    """Plot GC content along a sequence.
    
    Args:
        sequence: DNA/RNA sequence
        window_size: Size of sliding window
        step_size: Step size for sliding window
        title: Plot title
        
    Returns:
        matplotlib Figure object
    """
    sequence = sequence.upper()
    gc_content = []
    positions = []
    
    for i in range(0, len(sequence) - window_size + 1, step_size):
        window = sequence[i:i + window_size]
        gc = (window.count('G') + window.count('C')) / window_size * 100
        gc_content.append(gc)
        positions.append(i + window_size // 2)  # Center position
    
    # Create figure
    fig, ax = plt.subplots(figsize=(12, 4))
    
    # Plot GC content
    ax.plot(positions, gc_content, '-', color='#1f77b4', linewidth=2)
    
    # Add mean line
    mean_gc = (sequence.count('G') + sequence.count('C')) / len(sequence) * 100
    ax.axhline(mean_gc, color='r', linestyle='--', 
               label=f'Mean GC: {mean_gc:.1f}%')
    
    # Customize plot
    ax.set_xlim(0, len(sequence))
    ax.set_ylim(0, 100)
    ax.set_xlabel("Position (bp)")
    ax.set_ylabel("GC Content (%)")
    ax.set_title(title)
    ax.legend()
    
    plt.tight_layout()
    return fig

def plot_alignment(alignment: List[Tuple[str, str]], 
                   highlight_matches: bool = True,
                   title: str = "Sequence Alignment") -> plt.Figure:
    """Visualize a sequence alignment.
    
    Args:
        alignment: List of (header, sequence) tuples
        highlight_matches: Whether to highlight matching positions
        title: Plot title
        
    Returns:
        matplotlib Figure object
    """
    if not alignment:
        raise ValueError("No alignment data provided")
    
    headers, seqs = zip(*alignment)
    num_seqs = len(seqs)
    seq_len = len(seqs[0])
    
    # Create a grid for the alignment
    fig, ax = plt.subplots(figsize=(min(20, seq_len//2), num_seqs + 2))
    
    # Plot each sequence
    for i, (header, seq) in enumerate(alignment):
        y = num_seqs - i - 1  # Reverse order for top-to-bottom display
        
        # Plot sequence
        for j, nt in enumerate(seq.upper()):
            color = NUCLEOTIDE_COLORS.get(nt, '#CCCCCC')
            ax.add_patch(Rectangle(
                (j, y - 0.4), 1, 0.8,
                facecolor=color,
                edgecolor='white',
                linewidth=0.5
            ))
            
            # Add nucleotide letter
            ax.text(
                j + 0.5, y,
                nt,
                ha='center', va='center',
                color='white' if color.lower() != '#ffffff' else 'black',
                fontsize=8 if seq_len < 100 else 6
            )
    
    # Highlight matching positions
    if highlight_matches and len(seqs) > 1:
        for j in range(seq_len):
            column = [seq[j].upper() for seq in seqs]
            if all(nt == column[0] for nt in column[1:]):
                ax.add_patch(Rectangle(
                    (j, -0.5), 1, num_seqs,
                    facecolor='none',
                    edgecolor='black',
                    linewidth=1,
                    linestyle='--',
                    alpha=0.3
                ))
    
    # Customize plot
    ax.set_xlim(0, seq_len)
    ax.set_ylim(-1, num_seqs)
    ax.set_yticks(range(num_seqs))
    ax.set_yticklabels(headers)
    ax.set_xticks(range(0, seq_len, max(1, seq_len // 10)))
    ax.set_xlabel("Position")
    ax.set_title(title)
    
    plt.tight_layout()
    return fig

# Add interactive visualization functions if plotly is available
if PLOTLY_AVAILABLE:
    def interactive_gc_content(sequence: str, **kwargs) -> go.Figure:
        """Create an interactive GC content plot using plotly."""
        fig = plot_gc_content(sequence, **kwargs)
        plt.close()  # Close the matplotlib figure
        
        # Convert to plotly
        plotly_fig = go.Figure()
        
        # Add GC content line
        line = fig.axes[0].lines[0]
        plotly_fig.add_trace(go.Scatter(
            x=line.get_xdata(),
            y=line.get_ydata(),
            mode='lines',
            name='GC Content',
            line=dict(color='#1f77b4', width=2)
        ))
        
        # Add mean line
        mean_line = fig.axes[0].lines[1]
        plotly_fig.add_hline(
            y=mean_line.get_ydata()[0],
            line=dict(color='red', dash='dash'),
            annotation_text=f"Mean GC: {mean_line.get_ydata()[0]:.1f}%"
        )
        
        # Update layout
        plotly_fig.update_layout(
            title=fig.axes[0].get_title(),
            xaxis_title=fig.axes[0].get_xlabel(),
            yaxis_title=fig.axes[0].get_ylabel(),
            showlegend=True,
            hovermode='x'
        )
        
        return plotly_fig
