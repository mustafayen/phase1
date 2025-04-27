# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


import unittest

def string_sequence(n):
    return ''.join([str(i) for i in range(1, n+1)])

class TestStringSequence(unittest.TestCase):

    def test_string_sequence_5(self):
        self.assertEqual(string_sequence(5), '12345')

    def test_string_sequence_10(self):
        self.assertEqual(string_sequence(10), '12345678910')

    def test_string_sequence_1(self):
        self.assertEqual(string_sequence(1), '1')

    def test_string_sequence_0(self):
        self.assertEqual(string_sequence(0), '')

if __name__ == '__main__':
    unittest.main()