# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


import unittest

def flip_case(string):
    return string.swapcase()

class TestFlipCase(unittest.TestCase):

    def test_all_uppercase(self):
        self.assertEqual(flip_case("HELLO"), "hello")

    def test_all_lowercase(self):
        self.assertEqual(flip_case("hello"), "HELLO")

    def test_mixed_case(self):
        self.assertEqual(flip_case("HeLLo"), "hEllO")

    def test_empty_string(self):
        self.assertEqual(flip_case(""), "")

if __name__ == '__main__':
    unittest.main()