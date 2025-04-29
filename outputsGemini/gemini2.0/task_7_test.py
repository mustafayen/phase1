import unittest
from task_7_code import count_vowels # Import the function

class TestCountVowels(unittest.TestCase):

    def test_empty_string(self):
        """Test with an empty string."""
        self.assertEqual(count_vowels(""), 0)

    def test_string_with_only_vowels(self):
        """Test with a string containing only vowels."""
        self.assertEqual(count_vowels("aeiou"), 5)

    def test_string_with_only_consonants(self):
        """Test with a string containing only consonants."""
        self.assertEqual(count_vowels("bcdfgh"), 0)

    def test_string_with_mixed_case_vowels_and_consonants(self):
        """Test with a string containing mixed-case vowels and consonants."""
        self.assertEqual(count_vowels("Hello World"), 3)

    def test_string_with_special_characters(self):
        """Test with a string containing special characters."""
        self.assertEqual(count_vowels("a1b2c3d4e5"), 2)
