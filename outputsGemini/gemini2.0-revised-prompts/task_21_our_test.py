# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022


import unittest
from task_21_code import move_zeros

class TestTask21(unittest.TestCase):

    def test_case_1(self):
        nums = [0, 1, 0, 3, 12]
        move_zeros(nums)
        self.assertEqual(nums, [1, 3, 12, 0, 0])

    def test_case_2(self):
        nums = [0, 0, 0]
        move_zeros(nums)
        self.assertEqual(nums, [0, 0, 0])

    def test_case_3(self):
        nums = [1, 2, 3]
        move_zeros(nums)
        self.assertEqual(nums, [1, 2, 3])

    def test_case_4(self):
        nums = []
        move_zeros(nums)
        self.assertEqual(nums, [])

    def test_case_5(self):
        nums = [0, 0, 1]
        move_zeros(nums)
        self.assertEqual(nums, [1, 0, 0])

if __name__ == '__main__':
    unittest.main()
