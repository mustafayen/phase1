import unittest
from task_15_code import factorial # Import the function

class TestFactorial(unittest.TestCase):

    def test_factorial_of_0(self):
        """Test with n = 0."""
        self.assertEqual(factorial(0), 1)

    def test_factorial_of_1(self):
        """Test with n = 1."""
        self.assertEqual(factorial(1), 1)

    def test_factorial_of_positive_number(self):
        """Test with a positive number (n > 1)."""
        self.assertEqual(factorial(5), 120)

    def test_factorial_of_larger_number(self):
        """Test with a larger positive number."""
        self.assertEqual(factorial(10), 3628800)

    def test_factorial_of_negative_number(self):
        """Test with a negative number."""
        with self.assertRaises(ValueError):
            factorial(-1)
