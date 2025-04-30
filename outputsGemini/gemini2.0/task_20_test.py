import unittest
import numpy as np  # Import numpy for matrix equality comparison
from task_20_code import matrix_multiplication # Import the function

class TestMatrixMultiplication(unittest.TestCase):

    def test_valid_matrices(self):
        """Test with two valid matrices for multiplication."""
        A = [[1, 2], [3, 4]]
        B = [[5, 6], [7, 8]]
        expected_result = [[19, 22], [43, 50]]
        result = matrix_multiplication(A, B)
        self.assertTrue(np.array_equal(result, expected_result))

    def test_incompatible_matrices(self):
        """Test with matrices that are not compatible for multiplication."""
        A = [[1, 2], [3, 4]]
        B = [[5, 6, 7], [8, 9, 10]]
        self.assertIsNone(matrix_multiplication(A, B))

    def test_empty_matrix_A(self):
        """Test with an empty matrix A."""
        A = []
        B = [[1, 2], [3, 4]]
        self.assertIsNone(matrix_multiplication(A, B))

    def test_empty_matrix_B(self):
        """Test with an empty matrix B."""
        A = [[1, 2], [3, 4]]
        B = []
        self.assertIsNone(matrix_multiplication(A, B))
