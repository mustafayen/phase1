# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest

def check_brackets(string):
    stack = []
    brackets = {'(': ')', '[': ']', '{': '}'}
    
    for char in string:
        if char in brackets.keys():
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False
    
    return len(stack) == 0

class TestCheckBrackets(unittest.TestCase):
    
    def test_valid_brackets(self):
        self.assertTrue(check_brackets("()"))
        self.assertTrue(check_brackets("([])"))
        self.assertTrue(check_brackets("{()}"))
    
    def test_invalid_brackets(self):
        self.assertFalse(check_brackets("("))
        self.assertFalse(check_brackets(")"))
        self.assertFalse(check_brackets("([)]"))
        self.assertFalse(check_brackets("{[}]"))
    
    def test_mixed_brackets(self):
        self.assertFalse(check_brackets("({)}"))
        self.assertFalse(check_brackets("[{()}]"))
        self.assertTrue(check_brackets("{[()]}"))

if __name__ == '__main__':
    unittest.main()