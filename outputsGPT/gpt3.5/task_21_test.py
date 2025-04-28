# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest

def move_zeros(nums):
    zero_count = nums.count(0)
    nums = [num for num in nums if num != 0]
    nums.extend([0] * zero_count)
    return nums

class TestMoveZeros(unittest.TestCase):

    def test_move_zeros_no_zeros(self):
        self.assertEqual(move_zeros([1, 2, 3]), [1, 2, 3])

    def test_move_zeros_all_zeros(self):
        self.assertEqual(move_zeros([0, 0, 0]), [0, 0, 0])

    def test_move_zeros_mixed_zeros(self):
        self.assertEqual(move_zeros([0, 1, 0, 2, 0, 3]), [1, 2, 3, 0, 0, 0])

    def test_move_zeros_empty_list(self):
        self.assertEqual(move_zeros([]), [])

if __name__ == '__main__':
    unittest.main()