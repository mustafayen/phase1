# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from count_vowels import count_vowels

class TestCountVowels(unittest.TestCase):

    def test_count_vowels_empty_string(self):
        self.assertEqual(count_vowels(''), 0)

    def test_count_vowels_no_vowels(self):
        self.assertEqual(count_vowels('rhythm'), 0)

    def test_count_vowels_all_vowels(self):
        self.assertEqual(count_vowels('aeiou'), 5)

    def test_count_vowels_mixed_case(self):
        self.assertEqual(count_vowels('Hello World'), 3)

if __name__ == '__main__':
    unittest.main()