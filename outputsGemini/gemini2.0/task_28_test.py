import unittest
from task_28_code import zigzag_conversion # Import the function

class TestZigzagConversion(unittest.TestCase):

    def test_empty_string(self):
        """Test with an empty string."""
        self.assertEqual(zigzag_conversion("", 3), "")

    def test_one_row(self):
        """Test with one row."""
        self.assertEqual(zigzag_conversion("PAYPALISHIRING", 1), "PAYPALISHIRING")

    def test_two_rows(self):
        """Test with two rows."""
        self.assertEqual(zigzag_conversion("PAYPALISHIRING", 2), "PYAIHRNAPLSIIG")

    def test_three_rows(self):
        """Test with three rows."""
        self.assertEqual(zigzag_conversion("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")

    def test_four_rows(self):
        """Test with four rows."""
        self.assertEqual(zigzag_conversion("PAYPALISHIRING", 4), "PINALSIGYAHRPI")
