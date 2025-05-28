# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022


import unittest
from task_27_code import generate_parentheses

class TestTask27(unittest.TestCase):

    def test_case_1(self):
        self.assertIn("()", generate_parentheses(1))

    def test_case_2(self):
        result = generate_parentheses(2)
        self.assertTrue("()()" in result and "(())" in result)

    def test_case_3(self):
        self.assertEqual(len(generate_parentheses(3)), 5)

    def test_case_4(self):
        self.assertEqual(generate_parentheses(0), [""])

    def test_case_5(self):
        self.assertNotIn("(()", generate_parentheses(2))

if __name__ == '__main__':
    unittest.main()
