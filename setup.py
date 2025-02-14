from setuptools import setup, find_packages

setup(
    name="dna_sequence_analysis_tool",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'numpy>=1.19.0',
        'scipy>=1.5.0',
        'biopython>=1.78',
        'pandas>=1.2.0',
        'pytest>=6.0.0',
        'pytest-cov>=2.0.0',
        'matplotlib>=3.3.0',  # For visualization capabilities
        'seaborn>=0.11.0',   # For enhanced plotting
    ],
    python_requires='>=3.7',
    author="Yan Cotta",
    description="A high-performance Python library for comprehensive DNA sequence analysis",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/YanCotta/DNASequenceAnalysisTool",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
)