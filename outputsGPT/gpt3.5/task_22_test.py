# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from my_module import gcd

class TestGCDFunction(unittest.TestCase):

    def test_gcd_positive_numbers(self):
        result = gcd(10, 25)
        self.assertEqual(result, 5)

    def test_gcd_negative_numbers(self):
        result = gcd(-10, -25)
        self.assertEqual(result, 5)

    def test_gcd_one_negative_number(self):
        result = gcd(-10, 25)
        self.assertEqual(result, 5)

    def test_gcd_one_zero(self):
        result = gcd(0, 25)
        self.assertEqual(result, 25)

    def test_gcd_both_zeros(self):
        result = gcd(0, 0)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()