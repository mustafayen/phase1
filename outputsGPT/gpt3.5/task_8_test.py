# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest

def rotate_matrix(matrix):
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = temp
    return matrix

class TestRotateMatrix(unittest.TestCase):

    def test_rotate_2x2_matrix(self):
        matrix = [[1, 2], [3, 4]]
        rotated_matrix = rotate_matrix(matrix)
        self.assertEqual(rotated_matrix, [[3, 1], [4, 2]])

    def test_rotate_3x3_matrix(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        rotated_matrix = rotate_matrix(matrix)
        self.assertEqual(rotated_matrix, [[7, 4, 1], [8, 5, 2], [9, 6, 3]])

    def test_rotate_4x4_matrix(self):
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        rotated_matrix = rotate_matrix(matrix)
        self.assertEqual(rotated_matrix, [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]])

if __name__ == '__main__':
    unittest.main()