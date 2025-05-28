# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_27_code import generate_parentheses

class TestGenerateParentheses(unittest.TestCase):

    def test_generate_parentheses_1(self):
        n = 1
        self.assertEqual(generate_parentheses(n), ["()"])

    def test_generate_parentheses_2(self):
        n = 2
        self.assertEqual(generate_parentheses(n), ["(())", "()()"])

    def test_generate_parentheses_3(self):
        n = 3
        self.assertEqual(generate_parentheses(n), ["((()))", "(()())", "(())()", "()(())", "()()()"])

if __name__ == '__main__':
    unittest.main()