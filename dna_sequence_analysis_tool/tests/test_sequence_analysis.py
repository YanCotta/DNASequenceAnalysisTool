import unittest
import sys
import os

# Add the project directory to the PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from dna_sequence_analysis_tool.core.sequence_analysis import SequenceAnalyzer, AdvancedSequenceAnalyzer, AnalysisError, AdvancedAnalysisParameters

class TestSequenceAnalyzer(unittest.TestCase):

    def test_find_orfs(self):
        sequence = "ATGAAATAGATGCCCTAA"
        orfs = SequenceAnalyzer.find_orfs(sequence)
        self.assertEqual(len(orfs), 2)
        self.assertEqual(orfs[0][1], "ATGAAATAG")
        self.assertEqual(orfs[1][1], "ATGCCCTAA")

    def test_find_orfs_invalid_sequence(self):
        with self.assertRaises(AnalysisError):
            SequenceAnalyzer.find_orfs("INVALID")

    def test_find_repeats(self):
        sequence = "ATGATGATG"
        repeats = SequenceAnalyzer.find_repeats(sequence, min_length=3)
        self.assertIn("ATG", repeats)
        self.assertEqual(repeats["ATG"], [0, 3, 6])

    def test_find_repeats_invalid_sequence(self):
        with self.assertRaises(AnalysisError):
            SequenceAnalyzer.find_repeats("INVALID")

    def test_local_alignment(self):
        seq1 = "GATTACA"
        seq2 = "GCATGCU"
        alignment = SequenceAnalyzer.local_alignment(seq1, seq2)
        self.assertIn("score", alignment)

class TestAdvancedSequenceAnalyzer(unittest.TestCase):

    def test_predict_promoter_regions(self):
        sequence = "TATAATGCGTATA"
        promoters = AdvancedSequenceAnalyzer.predict_promoter_regions(sequence)
        self.assertTrue(len(promoters) > 0)

    def test_analyze_repeats(self):
        sequence = "ATGATGATG"
        params = AdvancedAnalysisParameters()
        analysis = AdvancedSequenceAnalyzer.analyze_repeats(sequence, params)
        self.assertIn("tandem_repeats", analysis)

    def test_local_alignment_affine(self):
        seq1 = "GATTACA"
        seq2 = "GCATGCU"
        params = AdvancedAnalysisParameters()
        alignment = AdvancedSequenceAnalyzer.local_alignment_affine(seq1, seq2, params)
        self.assertIn("score", alignment)

if __name__ == '__main__':
    unittest.main()
