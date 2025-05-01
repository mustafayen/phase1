# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_12_code import remove_duplicates

class TestRemoveDuplicates(unittest.TestCase):

    def test_remove_duplicates_empty_list(self):
        self.assertEqual(remove_duplicates([]), [])

    def test_remove_duplicates_no_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_remove_duplicates_with_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 3, 4]), [1, 2, 3, 4])

    def test_remove_duplicates_mixed_data_types(self):
        self.assertEqual(remove_duplicates([1, 'a', 'b', 'a', 2, 3, 3]), [1, 'a', 'b', 2, 3])

if __name__ == '__main__':  # pragma: no cover
    unittest.main()