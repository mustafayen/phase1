# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_16_code import is_palindrome

class TestIsPalindrome(unittest.TestCase):

    def test_palindrome_word(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_non_palindrome_word(self):
        self.assertFalse(is_palindrome("hello"))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_single_character_word(self):
        self.assertTrue(is_palindrome("a"))

if __name__ == '__main__':
    unittest.main()