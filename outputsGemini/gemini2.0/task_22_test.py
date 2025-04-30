import unittest
from task_22_code import gcd # Import the function

class TestGCD(unittest.TestCase):

    def test_positive_numbers(self):
        """Test with two positive integers."""
        self.assertEqual(gcd(12, 18), 6)

    def test_one_number_is_zero(self):
        """Test when one of the numbers is zero."""
        self.assertEqual(gcd(24, 0), 24)

    def test_both_numbers_are_zero(self):
        """Test when both numbers are zero."""
        self.assertEqual(gcd(0, 0), 0)

    def test_one_number_is_one(self):
        """Test when one of the numbers is one."""
        self.assertEqual(gcd(1, 10), 1)

    def test_numbers_are_relatively_prime(self):
        """Test with two numbers that are relatively prime (GCD is 1)."""
        self.assertEqual(gcd(7, 15), 1)
