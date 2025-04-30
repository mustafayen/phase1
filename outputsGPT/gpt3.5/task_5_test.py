# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_5_code import is_prime

class TestIsPrime(unittest.TestCase):

    def test_is_prime_with_prime_number(self):
        result = is_prime(7)
        self.assertTrue(result)

    def test_is_prime_with_non_prime_number(self):
        result = is_prime(4)
        self.assertFalse(result)

    def test_is_prime_with_negative_number(self):
        result = is_prime(-5)
        self.assertFalse(result)

    def test_is_prime_with_zero(self):
        result = is_prime(0)
        self.assertFalse(result)

    def test_is_prime_with_one(self):
        result = is_prime(1)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()