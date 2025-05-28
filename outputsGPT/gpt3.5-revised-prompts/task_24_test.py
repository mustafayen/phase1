# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_24_code import missing_number

class TestFindMissingNumber(unittest.TestCase):

    def test_missing_number_1(self):
        nums = [3, 0, 1]
        self.assertEqual(missing_number(nums), 2)

    def test_missing_number_2(self):
        nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
        self.assertEqual(missing_number(nums), 8)

    def test_missing_number_3(self):
        nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(missing_number(nums), 9)

    def test_missing_number_4(self):
        nums = [1, 0]
        self.assertEqual(missing_number(nums), 2)

if __name__ == '__main__':
    unittest.main()
