import unittest

from task_1_code import calculate_area

class TestMergeSortedLists(unittest.TestCase):

    def test_empty_lists(self):
        """Test with two empty lists."""
        list1 = []
        list2 = []
        expected_result = []
        self.assertEqual(merge_sorted_lists(list1, list2), expected_result)

    def test_one_empty_list(self):
        """Test with one empty list."""
        list1 = [1, 2, 3]
        list2 = []
        expected_result = [1, 2, 3]
        self.assertEqual(merge_sorted_lists(list1, list2), expected_result)

    def test_both_lists_with_elements(self):
        """Test with both lists containing elements."""
        list1 = [1, 3, 5]
        list2 = [2, 4, 6]
        expected_result = [1, 2, 3, 4, 5, 6]
        self.assertEqual(merge_sorted_lists(list1, list2), expected_result)

    def test_lists_with_duplicates(self):
        """Test with lists containing duplicate elements."""
        list1 = [1, 2, 2, 3]
        list2 = [2, 2, 4, 5]
        expected_result = [1, 2, 2, 2, 2, 3, 4, 5]
        self.assertEqual(merge_sorted_lists(list1, list2), expected_result)

    def test_one_list_larger_than_the_other(self):
        """Test when one list is significantly longer than the other."""
        list1 = [1, 2, 3, 4, 5, 6, 7]
        list2 = [2, 4]
        expected_result = [1, 2, 2, 3, 4, 4, 5, 6, 7]
        self.assertEqual(merge_sorted_lists(list1, list2), expected_result)
