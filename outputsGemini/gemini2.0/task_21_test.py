import unittest
from task_21_code import move_zeros # Import the function

class TestMoveZeros(unittest.TestCase):

    def test_empty_list(self):
        """Test with an empty list."""
        nums = []
        move_zeros(nums)
        self.assertEqual(nums, [])

    def test_zeros_at_end(self):
        """Test with zeros at the end of the list."""
        nums = [1, 2, 3, 0, 0]
        move_zeros(nums)
        self.assertEqual(nums, [1, 2, 3, 0, 0])

    def test_zeros_in_middle(self):
        """Test with zeros in the middle of the list."""
        nums = [1, 0, 2, 0, 3]
        move_zeros(nums)
        self.assertEqual(nums, [1, 2, 3, 0, 0])

    def test_mixed_numbers(self):
        """Test with a mix of positive, negative numbers and zeros."""
        nums = [0, 1, -2, 0, 3, -4, 0]
        move_zeros(nums)
        self.assertEqual(nums, [1, -2, 3, -4, 0, 0, 0])
