import unittest
from task_2_code import find_longest_word # Import the function

class TestFindLongestWord(unittest.TestCase):

    def test_empty_list(self):
        """Test with an empty list."""
        words = []
        expected_result = ""
        self.assertEqual(find_longest_word(words), expected_result)

    def test_single_word_list(self):
        """Test with a list containing a single word."""
        words = ["hello"]
        expected_result = "hello"
        self.assertEqual(find_longest_word(words), expected_result)

    def test_multiple_words_different_lengths(self):
        """Test with a list of words with different lengths."""
        words = ["apple", "banana", "kiwi", "strawberry"]
        expected_result = "strawberry"
        self.assertEqual(find_longest_word(words), expected_result)

    def test_multiple_words_same_length(self):
        """Test with a list of words where multiple words have the same longest length."""
        words = ["apple", "banana", "kiwi", "orange", "grape"]
        expected_result = "banana"  # The first longest word is returned
        self.assertEqual(find_longest_word(words), expected_result)

    def test_words_with_spaces(self):
        """Test with words containing spaces."""
        words = ["hello world", "python programming", "data science"]
        expected_result = "python programming"
        self.assertEqual(find_longest_word(words), expected_result)
