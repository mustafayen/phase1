# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_22_code import gcd

class TestGCDFunction(unittest.TestCase):

    def test_gcd_of_10_and_25(self):
        result = gcd(10, 25)
        self.assertEqual(result, 5)

    def test_gcd_of_21_and_28(self):
        result = gcd(21, 28)
        self.assertEqual(result, 7)

    def test_gcd_of_18_and_24(self):
        result = gcd(18, 24)
        self.assertEqual(result, 6)

    def test_gcd_of_0_and_5(self):
        result = gcd(0, 5)
        self.assertEqual(result, 5)

    def test_gcd_of_0_and_0(self):
        result = gcd(0, 0)
        self.assertEqual(result, 0)

if __name__ == '__main__':  # pragma: no cover
    unittest.main()