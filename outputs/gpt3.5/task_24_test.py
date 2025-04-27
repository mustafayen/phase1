# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


import unittest

def largest_divisor(n):
    max_divisor = 1
    for i in range(2, n+1):
        if n % i == 0:
            max_divisor = i
    return max_divisor

class TestLargestDivisor(unittest.TestCase):

    def test_largest_divisor_1(self):
        self.assertEqual(largest_divisor(10), 5)

    def test_largest_divisor_2(self):
        self.assertEqual(largest_divisor(15), 5)

    def test_largest_divisor_3(self):
        self.assertEqual(largest_divisor(25), 5)

    def test_largest_divisor_4(self):
        self.assertEqual(largest_divisor(7), 1)

    def test_largest_divisor_5(self):
        self.assertEqual(largest_divisor(100), 50)

if __name__ == '__main__':
    unittest.main()