import unittest
from task_17_code import find_pairs_with_sum # Import the function

class TestFindPairsWithSum(unittest.TestCase):

    def test_empty_list(self):
        """Test with an empty list."""
        numbers = []
        target = 10
        self.assertEqual(find_pairs_with_sum(numbers, target), [])

    def test_no_pairs_found(self):
        """Test when no pairs add up to the target."""
        numbers = [1, 2, 3, 4, 5]
        target = 100
        self.assertEqual(find_pairs_with_sum(numbers, target), [])

    def test_pairs_found(self):
        """Test when pairs are found."""
        numbers = [1, 2, 3, 4, 5]
        target = 6
        self.assertEqual(find_pairs_with_sum(numbers, target), [(1, 5), (2, 4)])

    def test_duplicate_numbers(self):
        """Test with duplicate numbers in the list."""
        numbers = [1, 2, 2, 3, 4]
        target = 4
        self.assertEqual(find_pairs_with_sum(numbers, target), [(1, 3), (2, 2)])

    def test_negative_numbers(self):
        """Test with negative numbers in the list."""
        numbers = [-1, -2, -3, 1, 2, 3]
        target = 0
        self.assertEqual(find_pairs_with_sum(numbers, target), [(-3, 3), (-2, 2), (-1, 1)])
