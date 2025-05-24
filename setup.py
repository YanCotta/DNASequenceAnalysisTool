from setuptools import setup, find_packages
import os
from pathlib import Path

# Read the README for the long description
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

# Read requirements
with open('requirements.txt', 'r', encoding='utf-8') as f:
    requirements = [
        line.strip() 
        for line in f.readlines() 
        if line.strip() and not line.startswith('#') and not line.startswith('-e')
    ]

# Filter out platform-specific dependencies
requirements = [
    req for req in requirements 
    if ';' not in req or any(platform in req.lower() for platform in ['win', 'linux', 'darwin'])
]

# Get package data files
def get_package_data(package_dir):
    """Get all non-Python files in the package directory."""
    package_data = []
    for root, _, files in os.walk(package_dir):
        for file in files:
            if not file.endswith('.py') and not file.endswith('.pyc'):
                path = Path(root) / file
                package_data.append(str(path.relative_to(package_dir)))
    return package_data

setup(
    name="dna_sequence_analysis_tool",
    version="0.2.0",
    packages=find_packages(exclude=['tests*', 'docs*', 'examples*']),
    install_requires=requirements,
    python_requires='>=3.8',
    
    # Metadata
    author="Yan Cotta",
    author_email="your.email@example.com",
    description="A high-performance Python library for comprehensive DNA sequence analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YanCotta/DNASequenceAnalysisTool",
    project_urls={
        'Bug Reports': 'https://github.com/YanCotta/DNASequenceAnalysisTool/issues',
        'Source': 'https://github.com/YanCotta/DNASequenceAnalysisTool',
        'Documentation': 'https://dna-sequence-analysis-tool.readthedocs.io/',
    },
    
    # Entry points
    entry_points={
        'console_scripts': [
            'dnatool=dna_sequence_analysis_tool.cli:cli',
        ],
    },
    
    # Additional files
    include_package_data=True,
    package_data={
        'dna_sequence_analysis_tool': ['data/*'],
    },
    
    # Classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Healthcare Industry',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        'Operating System :: OS Independent',
    ],
    
    # Keywords
    keywords='bioinformatics dna sequence analysis genomics',
    include_package_data=True,
    
    # Classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
        'Natural Language :: English',
    ],
    
    # Keywords
    keywords=[
        'bioinformatics', 
        'dna', 
        'sequence analysis', 
        'genomics', 
        'biotechnology'
    ],
    
    # Other
    zip_safe=False,
)