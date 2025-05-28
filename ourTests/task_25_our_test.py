# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022


import unittest
from task_25_code import check_brackets

class TestTask25(unittest.TestCase):

    def test_case_1(self):
        self.assertTrue(check_brackets("()"))

    def test_case_2(self):
        self.assertTrue(check_brackets("()[]{}"))

    def test_case_3(self):
        self.assertFalse(check_brackets("(]"))

    def test_case_4(self):
        self.assertFalse(check_brackets("([)]"))

    def test_case_5(self):
        self.assertTrue(check_brackets("{[]}"))

if __name__ == '__main__':
    unittest.main()
