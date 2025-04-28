# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from generate_parentheses import generate_parentheses

class TestGenerateParentheses(unittest.TestCase):

    def test_generate_parentheses_1(self):
        self.assertEqual(generate_parentheses(1), ["()"])

    def test_generate_parentheses_2(self):
        self.assertEqual(generate_parentheses(2), ["(())", "()()"])

    def test_generate_parentheses_3(self):
        self.assertEqual(generate_parentheses(3), ["((()))", "(()())", "(())()", "()(())", "()()()"])

    def test_generate_parentheses_4(self):
        self.assertEqual(generate_parentheses(4), ["(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())", "(()())()", "(())(())", "(())()()", "()((()))", "()(()())", "()(())()", "()()(())", "()()()()"])

if __name__ == '__main__':
    unittest.main()