# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_24_code import missing_number

class TestMissingNumber(unittest.TestCase):

    def test_missing_number_single_missing(self):
        nums = [1, 2, 3, 5]
        self.assertEqual(missing_number(nums), 4)

    def test_missing_number_multiple_missing(self):
        nums = [1, 2, 4, 5, 6, 8]
        self.assertEqual(missing_number(nums), 3)

    def test_missing_number_no_missing(self):
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(missing_number(nums), None)

    def test_missing_number_empty_list(self):
        nums = []
        self.assertEqual(missing_number(nums), None)

if __name__ == '__main__':  # pragma: no cover
    unittest.main()