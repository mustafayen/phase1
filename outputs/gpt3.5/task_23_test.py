# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


import unittest

def strlen(string):
    return len(string)

class TestStrlen(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(strlen(''), 0)

    def test_short_string(self):
        self.assertEqual(strlen('hello'), 5)

    def test_long_string(self):
        self.assertEqual(strlen('abcdefghijklmnopqrstuvwxyz'), 26)

    def test_special_characters(self):
        self.assertEqual(strlen('!@#$%^&*()'), 9)

if __name__ == '__main__':
    unittest.main()