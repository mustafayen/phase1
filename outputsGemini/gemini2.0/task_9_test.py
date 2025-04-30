import unittest
from task_9_code import reverse_string # Import the function

class TestReverseString(unittest.TestCase):

    def test_empty_string(self):
        """Test with an empty string."""
        self.assertEqual(reverse_string(""), "")

    def test_single_character_string(self):
        """Test with a string containing a single character."""
        self.assertEqual(reverse_string("a"), "a")

    def test_simple_string(self):
        """Test with a simple string."""
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_string_with_spaces(self):
        """Test with a string containing spaces."""
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")

    def test_string_with_special_characters(self):
        """Test with a string containing special characters."""
        self.assertEqual(reverse_string("!@#$%^"), "^%$#@!")
