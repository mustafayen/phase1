# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


import unittest

def make_palindrome(string):
    return string + string[::-1]

class TestMakePalindrome(unittest.TestCase):

    def test_make_palindrome_empty_string(self):
        self.assertEqual(make_palindrome(''), '')

    def test_make_palindrome_single_character(self):
        self.assertEqual(make_palindrome('a'), 'aa')

    def test_make_palindrome_even_length_string(self):
        self.assertEqual(make_palindrome('hello'), 'helloolleh')

    def test_make_palindrome_odd_length_string(self):
        self.assertEqual(make_palindrome('racecar'), 'racecarracecar')

if __name__ == '__main__':
    unittest.main()