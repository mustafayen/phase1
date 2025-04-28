# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest

def flatten_list(nested_list):
    flattened_list = []
    for sublist in nested_list:
        if isinstance(sublist, list):
            flattened_list.extend(flatten_list(sublist))
        else:
            flattened_list.append(sublist)
    return flattened_list

class TestFlattenList(unittest.TestCase):

    def test_flatten_list_single_level(self):
        nested_list = [1, 2, 3, 4]
        self.assertEqual(flatten_list(nested_list), [1, 2, 3, 4])

    def test_flatten_list_multiple_levels(self):
        nested_list = [1, [2, [3, 4]], 5]
        self.assertEqual(flatten_list(nested_list), [1, 2, 3, 4, 5])

    def test_flatten_list_empty_list(self):
        nested_list = []
        self.assertEqual(flatten_list(nested_list), [])

    def test_flatten_list_mixed_types(self):
        nested_list = [1, [2, 'a', [3, 4]], 5]
        self.assertEqual(flatten_list(nested_list), [1, 2, 'a', 3, 4, 5])

if __name__ == '__main__':
    unittest.main()