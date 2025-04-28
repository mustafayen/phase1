# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest

def is_palindrome(word):
    return word == word[::-1]

class TestIsPalindrome(unittest.TestCase):

    def test_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("hello"))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_single_character(self):
        self.assertTrue(is_palindrome("a"))

if __name__ == '__main__':
    unittest.main()