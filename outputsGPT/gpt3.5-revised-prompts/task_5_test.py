# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_5_code import is_prime

class TestIsPrime(unittest.TestCase):

    def test_small_prime(self):
        self.assertTrue(is_prime(3))  # Basic small prime

    def test_small_non_prime(self):
        self.assertFalse(is_prime(1))  # Edge case: 1 is not prime

    def test_large_prime(self):
        self.assertTrue(is_prime(997))  # Larger known prime

    def test_large_non_prime(self):
        self.assertFalse(is_prime(1000))  # Larger non-prime

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            is_prime("eleven")  # Should raise for non-integer input

if __name__ == '__main__':
    unittest.main()
