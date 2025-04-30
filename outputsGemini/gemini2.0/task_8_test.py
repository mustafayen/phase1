import unittest
from task_8_code import rotate_matrix # Import the function

class TestRotateMatrix(unittest.TestCase):

    def test_empty_matrix(self):
        """Test with an empty matrix."""
        matrix = []
        rotate_matrix(matrix)
        self.assertEqual(matrix, [])

    def test_1x1_matrix(self):
        """Test with a 1x1 matrix."""
        matrix = [[1]]
        rotate_matrix(matrix)
        self.assertEqual(matrix, [[1]])

    def test_2x2_matrix(self):
        """Test with a 2x2 matrix."""
        matrix = [[1, 2], [3, 4]]
        rotate_matrix(matrix)
        self.assertEqual(matrix, [[3, 1], [4, 2]])

    def test_3x3_matrix(self):
        """Test with a 3x3 matrix."""
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        rotate_matrix(matrix)
        self.assertEqual(matrix, [[7, 4, 1], [8, 5, 2], [9, 6, 3]])

    def test_4x4_matrix(self):
        """Test with a 4x4 matrix."""
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        rotate_matrix(matrix)
        self.assertEqual(matrix, [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]])
