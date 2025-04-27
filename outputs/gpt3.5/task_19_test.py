# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


import unittest

def sort_numbers(numbers):
    return sorted(numbers)

class TestSortNumbers(unittest.TestCase):

    def test_sort_numbers_empty_list(self):
        self.assertEqual(sort_numbers([]), [])

    def test_sort_numbers_single_number(self):
        self.assertEqual(sort_numbers([5]), [5])

    def test_sort_numbers_positive_numbers(self):
        self.assertEqual(sort_numbers([3, 1, 5, 2, 4]), [1, 2, 3, 4, 5])

    def test_sort_numbers_negative_numbers(self):
        self.assertEqual(sort_numbers([-3, -1, -5, -2, -4]), [-5, -4, -3, -2, -1])

if __name__ == '__main__':
    unittest.main()