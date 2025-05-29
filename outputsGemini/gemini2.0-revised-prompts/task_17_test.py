import unittest


# from task_17_code import find_pairs_with_sum # Uncomment if the function is in a separate file

# Re-pasting the REVISED function here for completeness.
# If your function is in task_17_code.py, remove this block.
def find_pairs_with_sum(numbers, target):
    """
    Finds all unique pairs of numbers in a list that add up to a target sum.

    Args:
        numbers: A list of integers.
        target: The target sum (integer).

    Returns:
        A list of tuples, where each tuple represents a pair of numbers
        that add up to the target sum.
        Returns an empty list if no such pairs exist.
    """
    pairs = set()  # Use a set of tuples to automatically handle uniqueness
    seen = set()  # To track numbers encountered so far

    for num in numbers:
        complement = target - num
        if complement in seen:
            pair = tuple(sorted((num, complement)))
            pairs.add(pair)
        seen.add(num)

    return sorted(list(pairs))  # Sort the list of pairs for consistent output


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
        # The expected output is already sorted, and the function now returns sorted.
        self.assertEqual(find_pairs_with_sum(numbers, target), [(1, 5), (2, 4)])

    def test_duplicate_numbers(self):
        """Test with duplicate numbers in the list."""
        numbers = [1, 2, 2, 3, 4]
        target = 4
        # (1,3) and (2,2) should be found.
        # The (2,2) case is correctly handled by the revised logic.
        self.assertEqual(find_pairs_with_sum(numbers, target), [(1, 3), (2, 2)])

    def test_negative_numbers(self):
        """Test with negative numbers in the list."""
        numbers = [-1, -2, -3, 1, 2, 3]
        target = 0
        # Expected pairs should be sorted for consistent testing
        self.assertEqual(find_pairs_with_sum(numbers, target), [(-3, 3), (-2, 2), (-1, 1)])

    def test_large_numbers_and_target(self):
        """Test with large numbers and target to ensure efficiency (though not directly tested here)."""
        numbers = [1000, 2000, 3000, 4000, 5000, 6000]
        target = 7000
        self.assertEqual(find_pairs_with_sum(numbers, target), [(1000, 6000), (2000, 5000), (3000, 4000)])

    def test_single_element_list(self):
        """Test with a single element list."""
        numbers = [5]
        target = 10
        self.assertEqual(find_pairs_with_sum(numbers, target), [])

    def test_target_zero_with_neg_and_pos(self):
        """Test with target 0 and mixed positive/negative numbers."""
        numbers = [-5, 0, 5]
        target = 0
        self.assertEqual(find_pairs_with_sum(numbers, target),
                         [(-5, 5)])  # Note: (0,0) is not found unless 0 appears twice

    def test_target_zero_with_two_zeros(self):
        """Test with target 0 and two zeros."""
        numbers = [0, 0, 1, 2]
        target = 0
        self.assertEqual(find_pairs_with_sum(numbers, target), [(0, 0)])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)