# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_20_code import matrix_multiplication

class TestMatrixMultiplication(unittest.TestCase):

    def test_matrix_multiplication_2x2(self):
        A = [[1, 2], [3, 4]]
        B = [[5, 6], [7, 8]]
        result = matrix_multiplication(A, B)
        self.assertEqual(result, [[19, 22], [43, 50]])

    def test_matrix_multiplication_3x3(self):
        A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
        result = matrix_multiplication(A, B)
        self.assertEqual(result, [[30, 24, 18], [84, 69, 54], [138, 114, 90]])

    def test_matrix_multiplication_2x3_and_3x2(self):
        A = [[1, 2, 3], [4, 5, 6]]
        B = [[7, 8], [9, 10], [11, 12]]
        result = matrix_multiplication(A, B)
        self.assertEqual(result, [[58, 64], [139, 154]])

if __name__ == '__main__':  # pragma: no cover
    unittest.main()