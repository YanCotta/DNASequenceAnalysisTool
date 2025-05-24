"""
Command Line Interface for DNA Sequence Analysis Tool
==================================================

This module provides a command-line interface for the DNA Sequence Analysis Tool,
offering easy access to common sequence analysis tasks.

Available Commands:
    analyze     - Analyze DNA/RNA sequences
    convert     - Convert between sequence formats
    view        - Visualize sequence data
    stats       - Calculate sequence statistics
"""

import os
import sys
from pathlib import Path
from typing import List, Optional, Tuple, Dict, Any

import click
from rich.console import Console
from rich.table import Table
from rich.progress import track

from .core import DNAToolkit, SequenceRecord
from .core.sequence_io import read_fasta, write_fasta, detect_format
from .core.visualization import plot_gc_content, plot_sequence_logo, plot_alignment
from .core.sequence_validation import SequenceValidator
from .core.sequence_statistics import SequenceStatistics

# Initialize console for rich output
console = Console()

# Initialize toolkit and statistics
TOOLKIT = DNAToolkit()
STATS = SequenceStatistics()

# Common options
INPUT_FILE_OPTION = click.option(
    '-i', '--input',
    type=click.Path(exists=True, dir_okay=False, path_type=Path),
    required=True,
    help='Input file (FASTA/FASTQ)'
)

OUTPUT_FILE_OPTION = click.option(
    '-o', '--output',
    type=click.Path(writable=True, dir_okay=False, path_type=Path),
    help='Output file (default: stdout)'
)

SEQUENCE_OPTION = click.option(
    '-s', '--sequence',
    help='Input sequence (alternative to --input)'
)

@click.group()
@click.version_option()
def cli():
    """DNA Sequence Analysis Tool - Command Line Interface"""
    pass

@cli.command()
@click.argument('input', type=click.Path(exists=True, dir_okay=False), required=False)
@click.option('--sequence', '-s', help='Input sequence (alternative to input file)')
@click.option('--gc-window', type=int, default=100, help='Window size for GC content analysis')
@click.option('--orfs/--no-orfs', default=True, help='Find open reading frames')
@click.option('--repeats/--no-repeats', default=True, help='Find repeated sequences')
@click.option('--output-format', type=click.Choice(['text', 'json', 'csv']), default='text')
def analyze(input, sequence, gc_window, orfs, repeats, output_format):
    """Analyze DNA/RNA sequences."""
    if not (input or sequence):
        raise click.UsageError("Either --input or --sequence must be provided")
    
    if input:
        # Read sequences from file
        file_format = detect_format(input)
        if file_format == 'fasta':
            sequences = list(read_fasta(input))
        else:
            raise click.UsageError(f"Unsupported file format: {file_format}")
    else:
        # Use provided sequence
        sequences = [SequenceRecord(sequence=sequence, id="input_sequence")]
    
    # Process each sequence
    results = []
    for record in track(sequences, description="Analyzing..."):
        analysis = TOOLKIT.analyze_sequence(record.sequence)
        
        result = {
            'id': record.id,
            'length': len(record.sequence),
            'gc_content': analysis.gc_content,
            'nucleotide_counts': analysis.nucleotide_counts,
            'complexity': analysis.complexity,
            'molecular_weight': analysis.molecular_weight
        }
        
        if orfs:
            result['orfs'] = TOOLKIT.basic_analyzer.find_orfs(record.sequence)
        
        if repeats and hasattr(analysis, 'repeats'):
            result['repeats'] = analysis.repeats
        
        results.append(result)
    
    # Output results
    if output_format == 'text':
        _display_text_results(results)
    elif output_format == 'json':
        import json
        click.echo(json.dumps(results, indent=2))
    elif output_format == 'csv':
        _display_csv_results(results)

def _display_text_results(results: List[Dict[str, Any]]) -> None:
    """Display analysis results in a formatted text table."""
    for result in results:
        table = Table(title=f"Analysis Results - {result['id']}")
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="green")
        
        # Basic info
        table.add_row("Sequence Length", str(result['length']))
        table.add_row("GC Content", f"{result['gc_content']:.2f}%")
        table.add_row("Sequence Complexity", f"{result['complexity']:.3f}")
        table.add_row("Molecular Weight", f"{result['molecular_weight']:.2f}")
        
        # Nucleotide counts
        counts = ", ".join(f"{k}: {v}" for k, v in result['nucleotide_counts'].items())
        table.add_row("Nucleotide Counts", counts)
        
        # ORFs if available
        if 'orfs' in result:
            orfs = result['orfs']
            table.add_row("ORFs Found", str(len(orfs)))
            for i, orf in enumerate(orfs[:3], 1):  # Show first 3 ORFs
                table.add_row(f"  ORF {i}", f"Pos: {orf[0]}, Len: {len(orf[1])}, Frame: {orf[2]}")
        
        console.print(table)

def _display_csv_results(results: List[Dict[str, Any]]) -> None:
    """Display analysis results in CSV format."""
    import csv
    import io
    
    if not results:
        return
    
    # Get all possible fields
    fieldnames = set()
    for result in results:
        fieldnames.update(result.keys())
    
    # Convert to list for consistent ordering
    fieldnames = sorted(fieldnames)
    
    # Write to string buffer
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    writer.writeheader()
    
    for result in results:
        # Convert complex types to strings
        row = {}
        for k, v in result.items():
            if isinstance(v, (list, dict)):
                row[k] = str(v)
            else:
                row[k] = v
        writer.writerow(row)
    
    click.echo(output.getvalue())

@cli.command()
@INPUT_FILE_OPTION
@OUTPUT_FILE_OPTION
@click.option('--format', '-f', type=click.Choice(['fasta', 'fastq']), 
              help='Output format (default: same as input)')
@click.option('--validate/--no-validate', default=True, help='Validate sequences')
@click.option('--allow-ambiguous/--strict', default=False, 
              help='Allow IUPAC ambiguity codes')
def convert(input: Path, output: Optional[Path], format: Optional[str], 
           validate: bool, allow_ambiguous: bool):
    """Convert between sequence file formats."""
    # Detect input format if not specified
    input_format = detect_format(input)
    output_format = format or input_format
    
    if not output_format:
        raise click.UsageError("Could not detect input format. Please specify with --format")
    
    # Read input
    if input_format == 'fasta':
        records = list(read_fasta(input, validate=validate, 
                                allow_ambiguous=allow_ambiguous))
    else:
        raise click.UsageError(f"Unsupported input format: {input_format}")
    
    # Write output
    if output_format == 'fasta':
        if output:
            write_fasta(records, output)
            console.print(f"[green]✓[/] Wrote {len(records)} sequences to {output}")
        else:
            # Write to stdout
            import sys
            write_fasta(records, sys.stdout)
    else:
        raise click.UsageError(f"Unsupported output format: {output_format}")

@cli.command()
@INPUT_FILE_OPTION
@click.option('--type', '-t', type=click.Choice(['gc', 'logo', 'alignment']), 
              default='gc', help='Type of visualization')
@click.option('--output', '-o', type=click.Path(writable=True, dir_okay=False),
              help='Output file (default: show plot)')
@click.option('--dpi', type=int, default=100, help='Figure DPI')
@click.option('--title', help='Plot title')
def visualize(input: Path, type: str, output: Optional[str], dpi: int, title: str):
    """Visualize sequence data."""
    if type == 'gc':
        # Read first sequence from file
        records = list(read_fasta(input))
        if not records:
            raise click.UsageError("No sequences found in input file")
        
        fig = plot_gc_content(
            records[0].sequence,
            title=title or f"GC Content - {records[0].id}"
        )
    
    elif type == 'logo':
        # Read all sequences
        records = list(read_fasta(input))
        if len(records) < 2:
            raise click.UsageError("At least 2 sequences are required for sequence logo")
        
        # Align sequences (simple left alignment for demo)
        max_len = max(len(r.sequence) for r in records)
        aligned = [r.sequence.ljust(max_len, '-') for r in records]
        
        fig = plot_sequence_logo(
            aligned,
            title=title or "Sequence Logo"
        )
    
    elif type == 'alignment':
        # Read all sequences
        records = list(read_fasta(input))
        if len(records) < 2:
            raise click.UsageError("At least 2 sequences are required for alignment")
        
        # Simple alignment for demo
        max_len = max(len(r.sequence) for r in records)
        aligned = [(r.id, r.sequence.ljust(max_len, '-')) for r in records]
        
        fig = plot_alignment(
            aligned,
            title=title or "Sequence Alignment"
        )
    
    # Save or show the plot
    if output:
        fig.savefig(output, dpi=dpi, bbox_inches='tight')
        console.print(f"[green]✓[/] Saved visualization to {output}")
    else:
        try:
            import matplotlib.pyplot as plt
            plt.show()
        except Exception as e:
            console.print(f"[red]Error displaying plot: {e}")

if __name__ == '__main__':
    cli()
