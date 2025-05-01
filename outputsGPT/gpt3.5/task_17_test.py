# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_17_code import find_pairs_with_sum

class TestFindPairsWithSum(unittest.TestCase):

    def test_find_pairs_with_sum(self):
        numbers = [1, 2, 3, 4, 5]
        target = 7
        self.assertEqual(find_pairs_with_sum(numbers, target), [(2, 5), (3, 4)])

    def test_find_pairs_with_sum_empty_list(self):
        numbers = []
        target = 10
        self.assertEqual(find_pairs_with_sum(numbers, target), [])

    def test_find_pairs_with_sum_no_pairs(self):
        numbers = [1, 2, 3, 4, 5]
        target = 10
        self.assertEqual(find_pairs_with_sum(numbers, target), [])

    def test_find_pairs_with_sum_negative_numbers(self):
        numbers = [-1, -2, 3, 4, 5]
        target = 2
        self.assertEqual(find_pairs_with_sum(numbers, target), [(-1, 3)])

if __name__ == '__main__':  # pragma: no cover
    unittest.main()