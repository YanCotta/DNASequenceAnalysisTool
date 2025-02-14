from setuptools import setup, find_packages

setup(
    name="dna_sequence_analysis_tool",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'numpy>=1.19.0',
        'scipy>=1.5.0',
        'biopython>=1.78',
        'pandas>=1.2.0',  # Add this for data handling
        'pytest>=6.0.0',  # Add testing dependencies
        'pytest-cov>=2.0.0',
    ],
    python_requires='>=3.7',
)