# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_28_code import zigzag_conversion

class TestZigzagConversion(unittest.TestCase):

    def test_zigzag_conversion_example1(self):
        s = "PAYPALISHIRING"
        num_rows = 3
        self.assertEqual(zigzag_conversion(s, num_rows), "PAHNAPLSIIGYIR")

    def test_zigzag_conversion_example2(self):
        s = "HELLOWORLD"
        num_rows = 4
        self.assertEqual(zigzag_conversion(s, num_rows), "HROEWLLLOD")

    def test_zigzag_conversion_empty_string(self):
        s = ""
        num_rows = 2
        self.assertEqual(zigzag_conversion(s, num_rows), "")

    def test_zigzag_conversion_single_row(self):
        s = "SINGLE"
        num_rows = 1
        self.assertEqual(zigzag_conversion(s, num_rows), "SINGLE")

if __name__ == '__main__':  # pragma: no cover
    unittest.main()