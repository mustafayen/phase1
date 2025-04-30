import unittest
from task_27_code import generate_parentheses # Import the function

class TestGenerateParentheses(unittest.TestCase):

    def test_n_equals_0(self):
        """Test with n = 0."""
        self.assertEqual(generate_parentheses(0), [""])

    def test_n_equals_1(self):
        """Test with n = 1."""
        self.assertEqual(generate_parentheses(1), ["()"])

    def test_n_equals_2(self):
        """Test with n = 2."""
        self.assertEqual(sorted(generate_parentheses(2)), sorted(["(())", "()()"]))

    def test_n_equals_3(self):
        """Test with n = 3."""
        self.assertEqual(sorted(generate_parentheses(3)), sorted(["((()))", "(()())", "()(())", "()()()", "(())()"]))

    def test_n_equals_4(self):
        """Test with n = 4."""
        expected = ["(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())", "(()())()", "(())(())", "()((()))", "()(()())", "()(())()", "()()(())", "()()()()", "((())())", "(()())()"]
        self.assertEqual(sorted(generate_parentheses(4)), sorted(expected))
