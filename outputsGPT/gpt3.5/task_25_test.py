# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_25_code import check_brackets

class TestCheckBrackets(unittest.TestCase):

    def test_valid_brackets(self):
        self.assertTrue(check_brackets("((()))"))
        self.assertTrue(check_brackets("()"))
        self.assertTrue(check_brackets("([])"))
    
    def test_invalid_brackets(self):
        self.assertFalse(check_brackets("(()"))
        self.assertFalse(check_brackets(")("))
        self.assertFalse(check_brackets("([)]"))

    def test_empty_string(self):
        self.assertTrue(check_brackets(""))
    
    def test_mixed_brackets(self):
        self.assertFalse(check_brackets("([)]"))
        self.assertTrue(check_brackets("([])"))
        self.assertFalse(check_brackets("([)]"))

if __name__ == '__main__':
    unittest.main()