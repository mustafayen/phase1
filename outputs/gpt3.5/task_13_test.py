# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


import unittest
from your_module import greatest_common_divisor

class TestGreatestCommonDivisor(unittest.TestCase):

    def test_gcd_of_10_and_25(self):
        result = greatest_common_divisor(10, 25)
        self.assertEqual(result, 5)

    def test_gcd_of_14_and_28(self):
        result = greatest_common_divisor(14, 28)
        self.assertEqual(result, 14)

    def test_gcd_of_21_and_49(self):
        result = greatest_common_divisor(21, 49)
        self.assertEqual(result, 7)

    def test_gcd_of_36_and_48(self):
        result = greatest_common_divisor(36, 48)
        self.assertEqual(result, 12)

if __name__ == '__main__':
    unittest.main()