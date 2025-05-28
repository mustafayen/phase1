# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_8_code import rotate_matrix

class TestTask8(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(rotate_matrix([[1, 2], [3, 4]]), [[3, 1], [4, 2]])

    def test_case_2(self):
        self.assertEqual(rotate_matrix([[1]]), [[1]])

    def test_case_3(self):
        self.assertEqual(rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                         [[7, 4, 1], [8, 5, 2], [9, 6, 3]])

    def test_case_4(self):
        self.assertEqual(rotate_matrix([]), [])

    def test_case_5(self):
        self.assertEqual(rotate_matrix([[1, 2], [3, 4], [5, 6]]), [[5, 3, 1], [6, 4, 2]])

if __name__ == '__main__':
    unittest.main()
