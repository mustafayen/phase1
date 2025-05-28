# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_5_code import is_prime

class TestIsPrime(unittest.TestCase):

    def test_is_prime(self):
        self.assertTrue(is_prime(2))

    def test_is_not_prime(self):
        self.assertFalse(is_prime(4))

    def test_is_prime_large_number(self):
        self.assertTrue(is_prime(997))

    def test_is_not_prime_large_number(self):
        self.assertFalse(is_prime(1000))

if __name__ == '__main__':
    unittest.main()