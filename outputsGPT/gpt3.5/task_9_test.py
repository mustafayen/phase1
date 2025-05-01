# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_9_code import reverse_string

class TestReverseString(unittest.TestCase):

    def test_reverse_string_empty(self):
        self.assertEqual(reverse_string(''), '')

    def test_reverse_string_single_char(self):
        self.assertEqual(reverse_string('a'), 'a')

    def test_reverse_string_even_length(self):
        self.assertEqual(reverse_string('hello'), 'olleh')

    def test_reverse_string_odd_length(self):
        self.assertEqual(reverse_string('python'), 'nohtyp')

if __name__ == '__main__':  # pragma: no cover
    unittest.main()