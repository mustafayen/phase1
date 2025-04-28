# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest

def merge_sorted_lists(list1, list2):
    return sorted(list1 + list2)

class TestMergeSortedLists(unittest.TestCase):

    def test_merge_sorted_lists(self):
        self.assertEqual(merge_sorted_lists([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])

    def test_merge_sorted_lists_empty_lists(self):
        self.assertEqual(merge_sorted_lists([], []), [])

    def test_merge_sorted_lists_one_empty_list(self):
        self.assertEqual(merge_sorted_lists([1, 2, 3], []), [1, 2, 3])

    def test_merge_sorted_lists_duplicate_elements(self):
        self.assertEqual(merge_sorted_lists([1, 2, 3], [2, 3, 4]), [1, 2, 2, 3, 3, 4])

if __name__ == '__main__':
    unittest.main()