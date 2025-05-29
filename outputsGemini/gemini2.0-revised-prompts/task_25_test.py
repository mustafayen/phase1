import unittest
from task_25_code import check_brackets # Import the function

class TestCheckBrackets(unittest.TestCase):

    def test_empty_string(self):
        """Test with an empty string."""
        self.assertTrue(check_brackets(""))

    def test_balanced_parentheses(self):
        """Test with balanced parentheses."""
        self.assertTrue(check_brackets("()"))
        self.assertTrue(check_brackets("(())"))

    def test_unbalanced_parentheses(self):
        """Test with unbalanced parentheses."""
        self.assertFalse(check_brackets("("))
        self.assertFalse(check_brackets(")"))
        self.assertFalse(check_brackets("(()"))
        self.assertFalse(check_brackets("())"))

    def test_balanced_mixed_brackets(self):
        """Test with balanced mixed brackets."""
        self.assertTrue(check_brackets("(){}[]"))
        self.assertTrue(check_brackets("([{}])"))
        self.assertTrue(check_brackets("{[()]}"))

    def test_unbalanced_mixed_brackets(self):
        """Test with unbalanced mixed brackets."""
        self.assertFalse(check_brackets("({)}"))
        self.assertFalse(check_brackets("[(])"))
        self.assertFalse(check_brackets("((("))
        self.assertFalse(check_brackets(")))"))
        self.assertFalse(check_brackets("{"))
        self.assertFalse(check_brackets("]"))
