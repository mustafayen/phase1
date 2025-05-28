# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022


import unittest
from task_28_code import zigzag_conversion

class TestTask28(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(zigzag_conversion("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")

    def test_case_2(self):
        self.assertEqual(zigzag_conversion("ABC", 1), "ABC")

    def test_case_3(self):
        self.assertEqual(zigzag_conversion("A", 2), "A")

    def test_case_4(self):
        self.assertEqual(zigzag_conversion("", 4), "")

    def test_case_5(self):
        self.assertEqual(zigzag_conversion("ABCD", 2), "ACBD")

if __name__ == '__main__':
    unittest.main()
