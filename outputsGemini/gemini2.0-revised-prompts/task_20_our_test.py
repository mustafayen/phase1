# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022


import unittest
from task_20_code import matrix_multiplication

class TestTask20(unittest.TestCase):

    def test_case_1(self):
        A = [[1, 2], [3, 4]]
        B = [[2, 0], [1, 2]]
        self.assertEqual(matrix_multiplication(A, B), [[4, 4], [10, 8]])

    def test_case_2(self):
        self.assertEqual(matrix_multiplication([[0]], [[0]]), [[0]])

    def test_case_3(self):
        self.assertEqual(matrix_multiplication([[1]], [[2]]), [[2]])

    def test_case_4(self):
        A = [[1, 2, 3]]
        B = [[1], [2], [3]]
        self.assertEqual(matrix_multiplication(A, B), [[14]])

    def test_case_5(self):
        A = [[1, 0], [0, 1]]
        B = [[5, 6], [7, 8]]
        self.assertEqual(matrix_multiplication(A, B), [[5, 6], [7, 8]])

if __name__ == '__main__':
    unittest.main()
