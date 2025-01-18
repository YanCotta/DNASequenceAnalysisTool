from setuptools import setup, find_packages

setup(
    name="dna_sequence_analysis_tool",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'biopython',  # Added biopython as a dependency
    ],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'dna_toolkit=dna_sequence_analysis_tool.core.main:main',  # Added entry point for CLI
        ],
    },
)