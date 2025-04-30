# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_10_code import anagram_check

class TestAnagramCheck(unittest.TestCase):

    def test_anagram_true(self):
        self.assertTrue(anagram_check("listen", "silent"))

    def test_anagram_false(self):
        self.assertFalse(anagram_check("hello", "world"))

    def test_anagram_empty_strings(self):
        self.assertTrue(anagram_check("", ""))

    def test_anagram_different_lengths(self):
        self.assertFalse(anagram_check("abc", "abcd"))

if __name__ == '__main__':
    unittest.main()