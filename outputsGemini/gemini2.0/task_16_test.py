import unittest
from task_16_code import is_palindrome # Import the function

class TestIsPalindrome(unittest.TestCase):

    def test_simple_palindrome(self):
        """Test with a simple palindrome."""
        self.assertTrue(is_palindrome("racecar"))

    def test_non_palindrome(self):
        """Test with a non-palindrome."""
        self.assertFalse(is_palindrome("hello"))

    def test_mixed_case_palindrome(self):
        """Test with a mixed-case palindrome."""
        self.assertTrue(is_palindrome("Racecar"))

    def test_empty_string(self):
        """Test with an empty string."""
        self.assertTrue(is_palindrome(""))
