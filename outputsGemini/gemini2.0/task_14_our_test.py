# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022


import unittest
from task_14_code import calculate_median

class TestTask14(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(calculate_median([1, 2, 3]), 2)

    def test_case_2(self):
        self.assertEqual(calculate_median([3, 1, 2, 4]), 2.5)

    def test_case_3(self):
        self.assertEqual(calculate_median([5]), 5)

    def test_case_4(self):
        self.assertEqual(calculate_median([5, 3, 1, 4, 2]), 3)

    def test_case_5(self):
        self.assertEqual(calculate_median([10, 20, 30, 40]), 25)

if __name__ == '__main__':
    unittest.main()
