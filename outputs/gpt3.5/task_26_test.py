# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


import unittest

def remove_duplicates(numbers):
    return list(set(numbers))

class TestRemoveDuplicates(unittest.TestCase):

    def test_remove_duplicates_empty_list(self):
        self.assertEqual(remove_duplicates([]), [])

    def test_remove_duplicates_no_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 3]), [1, 2, 3])

    def test_remove_duplicates_with_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 3, 3]), [1, 2, 3])

    def test_remove_duplicates_mixed_data_types(self):
        self.assertEqual(remove_duplicates([1, 'a', 'a', 2, 3]), [1, 'a', 2, 3])

if __name__ == '__main__':
    unittest.main()