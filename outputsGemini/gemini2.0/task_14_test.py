import unittest
from task_14_code import calculate_median # Import the function

class TestCalculateMedian(unittest.TestCase):

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(calculate_median([]))

    def test_odd_number_of_elements(self):
        """Test with a list containing an odd number of elements."""
        self.assertEqual(calculate_median([1, 3, 2]), 2)

    def test_even_number_of_elements(self):
        """Test with a list containing an even number of elements."""
        self.assertEqual(calculate_median([1, 2, 3, 4]), 2.5)

    def test_list_with_duplicates(self):
        """Test with a list containing duplicate elements."""
        self.assertEqual(calculate_median([1, 2, 2, 3, 4]), 2)

    def test_list_with_negative_numbers(self):
        """Test with a list containing negative numbers."""
        self.assertEqual(calculate_median([-1, -2, -3, -4]), -2.5)
