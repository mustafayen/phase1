import unittest
from task_4_code import fibonacci # Import the function

class TestFibonacci(unittest.TestCase):

    def test_fibonacci_of_0(self):
        """Test with n = 0."""
        self.assertEqual(fibonacci(0), 0)

    def test_fibonacci_of_1(self):
        """Test with n = 1."""
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_of_positive_number(self):
        """Test with a positive number (n > 1)."""
        self.assertEqual(fibonacci(6), 8)

    def test_fibonacci_of_large_number(self):
        """Test with a larger positive number."""
        self.assertEqual(fibonacci(10), 55)

    def test_fibonacci_of_negative_number(self):
        """Test with a negative number."""
        with self.assertRaises(ValueError):
            fibonacci(-1)
