# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022


import unittest
from task_5_code import is_prime

class TestIsPrime(unittest.TestCase):

    def test_prime(self):
        self.assertTrue(is_prime(7))

    def test_non_prime(self):
        self.assertFalse(is_prime(8))

    def test_edge_case_zero(self):
        self.assertFalse(is_prime(0))

    def test_edge_case_one(self):
        self.assertFalse(is_prime(1))

    def test_large_prime(self):
        self.assertTrue(is_prime(97))

    def test_negative(self):
        self.assertFalse(is_prime(-5))

if __name__ == '__main__':
    unittest.main()
