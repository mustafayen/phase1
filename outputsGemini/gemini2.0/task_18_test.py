import unittest
from task_18_code import group_anagrams # Import the function

class TestGroupAnagrams(unittest.TestCase):

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertEqual(group_anagrams([]), [])

    def test_no_anagrams(self):
        """Test with a list of words that are not anagrams."""
        words = ["hello", "world", "python"]
        self.assertEqual(group_anagrams(words), [["hello"], ["world"], ["python"]])

    def test_simple_anagrams(self):
        """Test with a list of simple anagrams."""
        words = ["listen", "silent", "enlist"]
        self.assertEqual(group_anagrams(words), [["listen", "silent", "enlist"]])

    def test_mixed_anagrams(self):
        """Test with a list of words with mixed anagrams and non-anagrams."""
        words = ["listen", "silent", "hello", "world", "enlist"]
        self.assertEqual(group_anagrams(words), [["listen", "silent", "enlist"], ["hello"], ["world"]])

    def test_anagrams_with_different_case(self):
        """Test with anagrams with different cases."""
        words = ["Listen", "silent", "enlist", "Silent"]
        self.assertEqual(group_anagrams(words), [["Listen", "silent", "enlist", "Silent"]])
