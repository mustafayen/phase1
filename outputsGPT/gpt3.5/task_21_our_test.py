# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022


import unittest
from task_21_code import move_zeros

class TestTask21(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(move_zeros([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])

    def test_case_2(self):
        self.assertEqual(move_zeros([0, 0, 0]), [0, 0, 0])

    def test_case_3(self):
        self.assertEqual(move_zeros([1, 2, 3]), [1, 2, 3])

    def test_case_4(self):
        self.assertEqual(move_zeros([]), [])

    def test_case_5(self):
        self.assertEqual(move_zeros([0, 0, 1]), [1, 0, 0])

if __name__ == '__main__':
    unittest.main()
