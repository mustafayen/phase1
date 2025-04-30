import unittest
from task_26_code import most_frequent_element # Import the function

class TestMostFrequentElement(unittest.TestCase):

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(most_frequent_element([]))

    def test_single_element_list(self):
        """Test with a list containing a single element."""
        self.assertEqual(most_frequent_element([5]), 5)

    def test_repeated_elements_list(self):
        """Test with a list containing repeated elements."""
        self.assertEqual(most_frequent_element([1, 2, 2, 3, 3, 3]), 3)

    def test_tie_for_most_frequent(self):
        """Test with a list where multiple elements have the same frequency."""
        self.assertEqual(most_frequent_element([1, 2, 2, 1, 3, 3]), 1)

    def test_list_with_negative_numbers(self):
        """Test with a list containing negative numbers."""
        self.assertEqual(most_frequent_element([-1, -2, -2, -3, -3, -3]), -3)
