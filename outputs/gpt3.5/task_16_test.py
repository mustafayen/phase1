# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


import unittest
from my_module import count_distinct_characters

class TestCountDistinctCharacters(unittest.TestCase):

    def test_count_distinct_characters_empty_string(self):
        self.assertEqual(count_distinct_characters(""), 0)

    def test_count_distinct_characters_all_distinct_characters(self):
        self.assertEqual(count_distinct_characters("abcdefg"), 7)

    def test_count_distinct_characters_repeated_characters(self):
        self.assertEqual(count_distinct_characters("hello"), 4)

    def test_count_distinct_characters_mixed_case(self):
        self.assertEqual(count_distinct_characters("Hello World"), 8)

if __name__ == '__main__':
    unittest.main()