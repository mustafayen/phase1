# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_16_code import is_palindrome

class TestIsPalindrome(unittest.TestCase):

    def test_palindrome_even(self):
        self.assertTrue(is_palindrome("abba"))

    def test_palindrome_odd(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("hello"))

    def test_case_sensitive(self):
        self.assertFalse(is_palindrome("RaceCar"))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

if __name__ == '__main__':
    unittest.main()
