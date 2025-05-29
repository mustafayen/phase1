# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022


import unittest
from task_2_code import find_longest_word

class TestFindLongestWord(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_longest_word(["apple", "banana", "cherry"]), "banana")

    def test_multiple_same_length(self):
        self.assertEqual(find_longest_word(["dog", "cat", "bat"]), "dog")

    def test_empty_list(self):
        self.assertIsNone(find_longest_word([]))

    def test_single_element(self):
        self.assertEqual(find_longest_word(["onlyone"]), "onlyone")

    def test_mixed_case(self):
        self.assertEqual(find_longest_word(["a", "abcd", "ABCDEF", "abc"]), "ABCDEF")

if __name__ == '__main__':
    unittest.main()
