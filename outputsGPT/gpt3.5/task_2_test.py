# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_2_code import find_longest_word

class TestFindLongestWord(unittest.TestCase):

    def test_find_longest_word_single_word(self):
        words = ['apple']
        self.assertEqual(find_longest_word(words), 'apple')

    def test_find_longest_word_multiple_words(self):
        words = ['banana', 'orange', 'strawberry']
        self.assertEqual(find_longest_word(words), 'strawberry')

    def test_find_longest_word_empty_list(self):
        words = []
        self.assertEqual(find_longest_word(words), None)

    def test_find_longest_word_equal_length_words(self):
        words = ['dog', 'cat', 'bat']
        self.assertEqual(find_longest_word(words), 'dog')

if __name__ == '__main__':  # pragma: no cover
    unittest.main()