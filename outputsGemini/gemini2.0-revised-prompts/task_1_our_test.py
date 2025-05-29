# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022


import unittest
from task_1_code import merge_sorted_lists

class TestMergeSortedLists(unittest.TestCase):

    def test_regular_merge(self):
        self.assertEqual(merge_sorted_lists([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])

    def test_empty_first_list(self):
        self.assertEqual(merge_sorted_lists([], [1, 2, 3]), [1, 2, 3])

    def test_empty_second_list(self):
        self.assertEqual(merge_sorted_lists([1, 2, 3], []), [1, 2, 3])

    def test_both_empty(self):
        self.assertEqual(merge_sorted_lists([], []), [])

    def test_with_duplicates(self):
        self.assertEqual(merge_sorted_lists([1, 2, 2], [2, 3]), [1, 2, 2, 2, 3])

if __name__ == '__main__':
    unittest.main()
