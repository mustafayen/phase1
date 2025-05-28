# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_21_code import move_zeros

class TestMoveZeros(unittest.TestCase):

    def test_move_zeros_example1(self):
        nums = [0, 1, 0, 3, 12]
        move_zeros(nums)
        self.assertEqual(nums, [1, 3, 12, 0, 0])

    def test_move_zeros_example2(self):
        nums = [0, 0, 0, 1, 2, 3]
        move_zeros(nums)
        self.assertEqual(nums, [1, 2, 3, 0, 0, 0])

    def test_move_zeros_empty_list(self):
        nums = []
        move_zeros(nums)
        self.assertEqual(nums, [])

    def test_move_zeros_no_zeros(self):
        nums = [1, 2, 3, 4]
        move_zeros(nums)
        self.assertEqual(nums, [1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()
