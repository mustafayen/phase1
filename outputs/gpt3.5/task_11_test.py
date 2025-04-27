# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


import unittest

def string_xor(a, b):
    result = ""
    for char1, char2 in zip(a, b):
        if char1 != char2:
            result += char1
        else:
            result += char2
    return result

class TestStringXor(unittest.TestCase):

    def test_string_xor_same_length(self):
        self.assertEqual(string_xor("1010", "1100"), "0110")

    def test_string_xor_different_length(self):
        self.assertEqual(string_xor("10101", "110"), "01101")

    def test_string_xor_empty_string(self):
        self.assertEqual(string_xor("", "1100"), "")

    def test_string_xor_empty_strings(self):
        self.assertEqual(string_xor("", ""), "")

if __name__ == '__main__':
    unittest.main()