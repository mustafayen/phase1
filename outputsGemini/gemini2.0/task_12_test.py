import unittest
from task_12_code import remove_duplicates # Import the function

class TestRemoveDuplicates(unittest.TestCase):

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertEqual(remove_duplicates([]), [])

    def test_list_with_no_duplicates(self):
        """Test with a list containing no duplicates."""
        self.assertEqual(remove_duplicates([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_list_with_duplicates(self):
        """Test with a list containing duplicate elements."""
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 4, 4, 5]), [1, 2, 3, 4, 5])

    def test_list_with_all_duplicates(self):
        """Test with a list where all elements are duplicates."""
        self.assertEqual(remove_duplicates([1, 1, 1, 1, 1]), [1])

    def test_list_with_mixed_data_types(self):
        """Test with a list containing mixed data types (which can be compared)."""
        self.assertEqual(remove_duplicates([1, "a", 1, "b", "a", 2]), [1, "a", "b", 2])
