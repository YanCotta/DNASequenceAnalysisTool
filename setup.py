from setuptools import setup, find_packages

setup(
    name='dna-sequence-analysis',
    version='2.0.0',
    description='A high-performance Python library for comprehensive DNA sequence analysis.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Yan Cotta',
    author_email='yanpcotta@gmail.com',
    url='https://github.com/YanCotta/DNASequenceAnalysisTool',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.19.0',
        'biopython>=1.78',
        'pandas>=1.2.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'dna-toolkit=dna_sequence_analysis_tool.core.main:main',
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
