# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


import unittest

def concatenate(strings):
    return "".join(strings)

class TestConcatenate(unittest.TestCase):

    def test_concatenate_empty_list(self):
        self.assertEqual(concatenate([]), "")

    def test_concatenate_single_string(self):
        self.assertEqual(concatenate(["hello"]), "hello")

    def test_concatenate_multiple_strings(self):
        self.assertEqual(concatenate(["hello", "world"]), "helloworld")

    def test_concatenate_with_special_characters(self):
        self.assertEqual(concatenate(["hello", "!", "@"]), "hello!@")

if __name__ == '__main__':
    unittest.main()