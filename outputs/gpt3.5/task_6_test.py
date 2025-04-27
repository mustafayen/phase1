# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


import unittest

def parse_nested_parens(paren_string):
    stack = []
    result = []
    
    for char in paren_string:
        if char == '(':
            stack.append(result)
            result = []
        elif char == ')':
            temp = stack.pop()
            temp.append(result)
            result = temp
        else:
            result.append(char)
    
    return result

class TestParseNestedParens(unittest.TestCase):
    
    def test_single_nested_parens(self):
        self.assertEqual(parse_nested_parens("(abc)"), ['abc'])
    
    def test_multiple_nested_parens(self):
        self.assertEqual(parse_nested_parens("(abc(def)ghi)"), ['abc', ['def'], 'ghi'])
    
    def test_no_nested_parens(self):
        self.assertEqual(parse_nested_parens("abc(def)ghi"), ['abc(def)ghi'])
    
    def test_empty_string(self):
        self.assertEqual(parse_nested_parens(""), [])
    
    def test_nested_parens_with_empty_string(self):
        self.assertEqual(parse_nested_parens("(abc()def)"), ['abc', [], 'def'])

if __name__ == '__main__':
    unittest.main()