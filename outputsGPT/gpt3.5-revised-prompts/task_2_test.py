# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_2_code import longest_word

class TestLongestWord(unittest.TestCase):

    def test_longest_word_single(self):
        self.assertEqual(longest_word(["apple", "banana", "cherry"]), "banana")

    def test_longest_word_multiple(self):
        self.assertEqual(longest_word(["cat", "dog", "elephant", "giraffe"]), "elephant")

    def test_longest_word_same_length(self):
        self.assertEqual(longest_word(["apple", "banana", "cherry", "dog", "elephant"]), "banana")

    def test_longest_word_empty_list(self):
        self.assertEqual(longest_word([]), "")

if __name__ == '__main__':
    unittest.main()
