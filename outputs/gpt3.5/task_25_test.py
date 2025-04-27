# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


import unittest
from my_module import factorize

class TestFactorize(unittest.TestCase):

    def test_factorize_1(self):
        self.assertEqual(factorize(1), [1])

    def test_factorize_10(self):
        self.assertEqual(factorize(10), [1, 2, 5, 10])

    def test_factorize_15(self):
        self.assertEqual(factorize(15), [1, 3, 5, 15])

    def test_factorize_25(self):
        self.assertEqual(factorize(25), [1, 5, 25])

if __name__ == '__main__':
    unittest.main()