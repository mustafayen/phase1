# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest

def matrix_multiplication(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            total = 0
            for k in range(len(B)):
                total += A[i][k] * B[k][j]
            row.append(total)
        result.append(row)
    return result

class TestMatrixMultiplication(unittest.TestCase):

    def test_matrix_multiplication_2x2(self):
        A = [[1, 2], [3, 4]]
        B = [[5, 6], [7, 8]]
        self.assertEqual(matrix_multiplication(A, B), [[19, 22], [43, 50]])

    def test_matrix_multiplication_2x3(self):
        A = [[1, 2, 3], [4, 5, 6]]
        B = [[7, 8], [9, 10], [11, 12]]
        self.assertEqual(matrix_multiplication(A, B), [[58, 64], [139, 154]])

    def test_matrix_multiplication_3x2(self):
        A = [[1, 2], [3, 4], [5, 6]]
        B = [[7, 8, 9], [10, 11, 12]]
        self.assertEqual(matrix_multiplication(A, B), [[27, 30, 33], [61, 68, 75], [95, 106, 117]])

if __name__ == '__main__':
    unittest.main()