# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


import unittest

def longest(strings):
    return max(strings, key=len)

class TestLongest(unittest.TestCase):

    def test_longest_string(self):
        self.assertEqual(longest(["apple", "banana", "cherry"]), "banana")

    def test_empty_list(self):
        self.assertEqual(longest([]), None)

    def test_equal_length_strings(self):
        self.assertEqual(longest(["cat", "dog", "bat"]), "cat")

    def test_special_characters(self):
        self.assertEqual(longest(["!@#$%", "12345", "abcdefg"]), "!@#$%")

if __name__ == '__main__':
    unittest.main()