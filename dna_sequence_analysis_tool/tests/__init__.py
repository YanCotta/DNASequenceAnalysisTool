# Initialize the tests module
import unittest

def load_tests(loader, tests, pattern):
    return unittest.defaultTestLoader.discover('dna_sequence_analysis_tool/tests', pattern='test_*.py')

# ...existing code...
