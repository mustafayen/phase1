# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_8_code import rotate_matrix

class TestRotateMatrix(unittest.TestCase):

    def test_rotate_matrix_3x3(self):
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
        expected_output = [[7, 4, 1],
                           [8, 5, 2],
                           [9, 6, 3]]
        self.assertEqual(rotate_matrix(matrix), expected_output)

    def test_rotate_matrix_4x4(self):
        matrix = [[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]]
        expected_output = [[13, 9, 5, 1],
                           [14, 10, 6, 2],
                           [15, 11, 7, 3],
                           [16, 12, 8, 4]]
        self.assertEqual(rotate_matrix(matrix), expected_output)

    def test_rotate_matrix_2x2(self):
        matrix = [[1, 2],
                  [3, 4]]
        expected_output = [[3, 1],
                           [4, 2]]
        self.assertEqual(rotate_matrix(matrix), expected_output)

if __name__ == '__main__':
    unittest.main()
