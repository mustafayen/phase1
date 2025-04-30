# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_8_code import rotate_matrix

class TestRotateMatrix(unittest.TestCase):

    def test_rotate_matrix_90_degrees(self):
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
        expected_output = [[7, 4, 1],
                           [8, 5, 2],
                           [9, 6, 3]]
        self.assertEqual(rotate_matrix(matrix), expected_output)

    def test_rotate_matrix_180_degrees(self):
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
        expected_output = [[9, 8, 7],
                           [6, 5, 4],
                           [3, 2, 1]]
        self.assertEqual(rotate_matrix(matrix), expected_output)

    def test_rotate_matrix_270_degrees(self):
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
        expected_output = [[3, 6, 9],
                           [2, 5, 8],
                           [1, 4, 7]]
        self.assertEqual(rotate_matrix(matrix), expected_output)

if __name__ == '__main__':
    unittest.main()