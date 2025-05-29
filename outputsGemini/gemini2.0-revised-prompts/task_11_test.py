import unittest
from task_11_code import flatten_list # Import the function

class TestFlattenList(unittest.TestCase):

    def test_empty_list(self):
        """Test with an empty list."""
        nested_list = []
        self.assertEqual(flatten_list(nested_list), [])

    def test_flat_list(self):
        """Test with a list that is already flat."""
        nested_list = [1, 2, 3, 4, 5]
        self.assertEqual(flatten_list(nested_list), [1, 2, 3, 4, 5])

    def test_one_level_nesting(self):
        """Test with one level of nesting."""
        nested_list = [1, [2, 3], 4, 5]
        self.assertEqual(flatten_list(nested_list), [1, 2, 3, 4, 5])

    def test_multiple_levels_of_nesting(self):
        """Test with multiple levels of nesting."""
        nested_list = [1, [2, [3, 4]], 5]
        self.assertEqual(flatten_list(nested_list), [1, 2, 3, 4, 5])

    def test_deep_nesting(self):
        """Test with deep nesting."""
        nested_list = [1, [2, [3, [4, 5, [6]]]]]
        self.assertEqual(flatten_list(nested_list), [1, 2, 3, 4, 5, 6])
