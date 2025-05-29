import unittest
from task_5_code import is_prime

class TestIsPrime(unittest.TestCase):

    def test_is_prime_with_numbers_less_than_2(self):
        """Test with 0, 1, and a negative number (should all be False)."""
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(-5)) # Covers negative numbers

    def test_is_prime_with_2(self):
        """Test with the smallest prime number."""
        self.assertTrue(is_prime(2))

    def test_is_prime_with_a_small_composite_number(self):
        """Test with a small non-prime number (e.g., 4)."""
        self.assertFalse(is_prime(4))

    def test_is_prime_with_a_larger_prime_number(self):
        """Test with a larger prime number where the loop runs."""
        self.assertTrue(is_prime(17)) # A prime number whose loop will iterate

    def test_is_prime_with_a_larger_composite_number(self):
        """Test with a larger composite number where the loop finds a factor."""
        self.assertFalse(is_prime(25)) # 5 * 5, loop will find 5 as a factor

