# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_11_code import flatten_list

class TestFlattenList(unittest.TestCase):

    def test_flatten_list_empty(self):
        nested_list = []
        self.assertEqual(flatten_list(nested_list), [])

    def test_flatten_list_single_level(self):
        nested_list = [1, 2, 3]
        self.assertEqual(flatten_list(nested_list), [1, 2, 3])

    def test_flatten_list_multiple_levels(self):
        nested_list = [1, [2, 3], [4, [5, 6]]]
        self.assertEqual(flatten_list(nested_list), [1, 2, 3, 4, 5, 6])

    def test_flatten_list_mixed_data_types(self):
        nested_list = [1, [2, 'a'], ['b', [5, 6]]]
        self.assertEqual(flatten_list(nested_list), [1, 2, 'a', 'b', 5, 6])

if __name__ == '__main__':
    unittest.main()