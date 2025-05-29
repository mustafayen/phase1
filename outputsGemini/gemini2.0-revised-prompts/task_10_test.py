import unittest
from task_10_code import anagram_check # Import the function

class TestAnagramCheck(unittest.TestCase):

    def test_empty_strings(self):
        """Test with two empty strings."""
        self.assertTrue(anagram_check("", ""))

    def test_simple_anagrams(self):
        """Test with simple anagrams."""
        self.assertTrue(anagram_check("listen", "silent"))

    def test_non_anagrams(self):
        """Test with strings that are not anagrams."""
        self.assertFalse(anagram_check("hello", "world"))

    def test_anagrams_with_spaces(self):
        """Test with anagrams containing spaces."""
        self.assertTrue(anagram_check("conversation", "conservation "))

    def test_anagrams_with_different_case(self):
        """Test with anagrams having different letter cases."""
        self.assertTrue(anagram_check("Triangle", "Integral"))
