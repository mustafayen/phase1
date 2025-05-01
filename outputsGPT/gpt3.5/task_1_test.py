# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_1_code import merge_sorted_lists

class TestMergeSortedLists(unittest.TestCase):

    def test_merge_sorted_lists(self):
        list1 = [1, 3, 5]
        list2 = [2, 4, 6]
        expected_output = [1, 2, 3, 4, 5, 6]
        self.assertEqual(merge_sorted_lists(list1, list2), expected_output)

    def test_merge_sorted_lists_empty_list(self):
        list1 = []
        list2 = [2, 4, 6]
        expected_output = [2, 4, 6]
        self.assertEqual(merge_sorted_lists(list1, list2), expected_output)

    def test_merge_sorted_lists_duplicate_values(self):
        list1 = [1, 3, 5]
        list2 = [3, 4, 6]
        expected_output = [1, 3, 3, 4, 5, 6]
        self.assertEqual(merge_sorted_lists(list1, list2), expected_output)

    def test_merge_sorted_lists_negative_values(self):
        list1 = [-5, -3, -1]
        list2 = [-6, -4, -2]
        expected_output = [-6, -5, -4, -3, -2, -1]
        self.assertEqual(merge_sorted_lists(list1, list2), expected_output)

if __name__ == '__main__':  # pragma: no cover
    unittest.main()