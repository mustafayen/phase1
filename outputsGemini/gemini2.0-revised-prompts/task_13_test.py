import unittest
from task_13_code import get_unique_elements # Import the function

class TestGetUniqueElements(unittest.TestCase):

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertEqual(get_unique_elements([]), [])

    def test_list_with_no_duplicates(self):
        """Test with a list containing no duplicates."""
        self.assertEqual(get_unique_elements([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_list_with_duplicates(self):
        """Test with a list containing duplicate elements."""
        self.assertEqual(get_unique_elements([1, 2, 2, 3, 4, 4, 5]), [1, 2, 3, 4, 5])

    def test_list_with_all_duplicates(self):
        """Test with a list where all elements are duplicates."""
        self.assertEqual(get_unique_elements([1, 1, 1, 1, 1]), [1])

    def test_list_with_mixed_data_types(self):
        """Test with a list containing mixed data types."""
        self.assertEqual(get_unique_elements([1, "a", 1, "b", "a", 2]), [1, "a", "b", 2])
