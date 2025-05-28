# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_9_code import reverse_string

class TestReverseString(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_reverse_string_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_reverse_string_numbers(self):
        self.assertEqual(reverse_string("12345"), "54321")

    def test_reverse_string_special_characters(self):
        self.assertEqual(reverse_string("!@#$%"), "%$#@!")

if __name__ == '__main__':
    unittest.main()