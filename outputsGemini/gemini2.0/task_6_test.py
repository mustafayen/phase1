import unittest
from task_6_code import sum_even_numbers

class TestSumEvenNumbers(unittest.TestCase):

    def test_empty_list(self):
        """Test with an empty list."""
        numbers = []
        self.assertEqual(sum_even_numbers(numbers), 0)

    def test_list_with_only_even_numbers(self):
        """Test with a list containing only even numbers."""
        numbers = [2, 4, 6, 8]
        self.assertEqual(sum_even_numbers(numbers), 20)

    def test_list_with_only_odd_numbers(self):
        """Test with a list containing only odd numbers."""
        numbers = [1, 3, 5, 7]
        self.assertEqual(sum_even_numbers(numbers), 0)

    def test_list_with_mixed_numbers(self):
        """Test with a list containing both even and odd numbers."""
        numbers = [1, 2, 3, 4, 5, 6]
        self.assertEqual(sum_even_numbers(numbers), 12)

    def test_list_with_negative_numbers(self):
        """Test with a list containing negative numbers."""
        numbers = [-2, -4, -6, -8]
        self.assertEqual(sum_even_numbers(numbers), -20)
