# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_22_code import gcd

class TestGCDFunction(unittest.TestCase):

    def test_gcd_of_10_and_5(self):
        result = gcd(10, 5)
        self.assertEqual(result, 5)

    def test_gcd_of_21_and_14(self):
        result = gcd(21, 14)
        self.assertEqual(result, 7)

    def test_gcd_of_36_and_48(self):
        result = gcd(36, 48)
        self.assertEqual(result, 12)

    def test_gcd_of_17_and_23(self):
        result = gcd(17, 23)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()