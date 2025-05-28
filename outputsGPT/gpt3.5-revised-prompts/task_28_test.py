# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_28_code import convert_to_zigzag

class TestConvertToZigzag(unittest.TestCase):

    def test_example_1(self):
        s = "PAYPALISHIRING"
        num_rows = 3
        expected_output = "PAHNAPLSIIGYIR"
        self.assertEqual(convert_to_zigzag(s, num_rows), expected_output)

    def test_example_2(self):
        s = "HELLOWORLD"
        num_rows = 4
        expected_output = "HROEWOLLDEL"
        self.assertEqual(convert_to_zigzag(s, num_rows), expected_output)

    def test_single_row(self):
        s = "SINGLE"
        num_rows = 1
        expected_output = "SINGLE"
        self.assertEqual(convert_to_zigzag(s, num_rows), expected_output)

    def test_two_rows(self):
        s = "TWOROWS"
        num_rows = 2
        expected_output = "TWRWOSO"
        self.assertEqual(convert_to_zigzag(s, num_rows), expected_output)

    def test_large_input(self):
        s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        num_rows = 5
        expected_output = "AIQBHJPRCGKOSDFLNTVEMU"
        self.assertEqual(convert_to_zigzag(s, num_rows), expected_output)

if __name__ == '__main__':
    unittest.main()
