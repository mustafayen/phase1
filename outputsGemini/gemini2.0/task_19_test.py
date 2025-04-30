import unittest
from task_19_code import binary_search # Import the function

class TestBinarySearch(unittest.TestCase):

    def test_empty_array(self):
        """Test with an empty array."""
        self.assertEqual(binary_search([], 5), -1)

    def test_target_not_present(self):
        """Test when the target is not in the array."""
        arr = [2, 5, 8, 12, 16]
        self.assertEqual(binary_search(arr, 10), -1)

    def test_target_at_beginning(self):
        """Test when the target is at the beginning of the array."""
        arr = [2, 5, 8, 12, 16]
        self.assertEqual(binary_search(arr, 2), 0)

    def test_target_at_end(self):
        """Test when the target is at the end of the array."""
        arr = [2, 5, 8, 12, 16]
        self.assertEqual(binary_search(arr, 16), 4)
