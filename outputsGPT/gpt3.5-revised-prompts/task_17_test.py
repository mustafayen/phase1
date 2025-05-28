# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_17_code import find_pairs

class TestFindPairs(unittest.TestCase):

    def test_unique_pairs(self):
        numbers = [1, 2, 3, 4, 5]
        target = 6
        self.assertEqual(find_pairs(numbers, target), [(1, 5), (2, 4)])

    def test_no_pairs(self):
        numbers = [1, 2, 3, 4, 5]
        target = 10
        self.assertEqual(find_pairs(numbers, target), [])

    def test_duplicate_pairs(self):
        numbers = [2, 3, 3, 4, 5]
        target = 6
        self.assertEqual(find_pairs(numbers, target), [(2, 4), (3, 3)])

    def test_negative_numbers(self):
        numbers = [-1, 2, 3, -4, 5]
        target = 1
        self.assertEqual(find_pairs(numbers, target), [(-1, 2), (3, -4)])

if __name__ == '__main__':
    unittest.main()
