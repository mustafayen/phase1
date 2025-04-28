# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from my_module import is_prime

class TestIsPrime(unittest.TestCase):

    def test_is_prime_with_prime_number(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))

    def test_is_prime_with_non_prime_number(self):
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))

    def test_is_prime_with_negative_number(self):
        self.assertFalse(is_prime(-2))
        self.assertFalse(is_prime(-3))
        self.assertFalse(is_prime(-5))

if __name__ == '__main__':
    unittest.main()