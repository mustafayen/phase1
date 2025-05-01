# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_21_code import move_zeros

class TestMoveZeros(unittest.TestCase):

    def test_all_zeros(self):
        nums = [0, 0, 0, 0]
        expected = [0, 0, 0, 0]
        move_zeros(nums)
        self.assertEqual(nums, expected)

    def test_no_zeros(self):
        nums = [1, 2, 3, 4]
        expected = [1, 2, 3, 4]
        move_zeros(nums)
        self.assertEqual(nums, expected)

    def test_mixed_numbers(self):
        nums = [0, 1, 0, 3, 0, 5]
        expected = [1, 3, 5, 0, 0, 0]
        move_zeros(nums)
        self.assertEqual(nums, expected)

    def test_empty_list(self):
        nums = []
        expected = []
        move_zeros(nums)
        self.assertEqual(nums, expected)

if __name__ == '__main__':  # pragma: no cover
    unittest.main()