import unittest
from task_23_code import lcm # Import the function

class TestLCM(unittest.TestCase):

    def test_positive_numbers(self):
        """Test with two positive integers."""
        self.assertEqual(lcm(12, 18), 36)

    def test_one_number_is_zero(self):
        """Test when one of the numbers is zero."""
        self.assertEqual(lcm(24, 0), 0)

    def test_both_numbers_are_zero(self):
        """Test when both numbers are zero."""
        self.assertEqual(lcm(0, 0), 0)

    def test_one_number_is_one(self):
        """Test when one of the numbers is one."""
        self.assertEqual(lcm(1, 10), 10)

    def test_numbers_are_relatively_prime(self):
        """Test with two numbers that are relatively prime (LCM is their product)."""
        self.assertEqual(lcm(7, 15), 105)
