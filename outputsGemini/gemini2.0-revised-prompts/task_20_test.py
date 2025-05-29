import unittest
from task_20_code import matrix_multiplication

class TestMatrixMultiplication(unittest.TestCase):

    def test_incompatible_matrices(self):
        # Fix: Provided matrices are truly incompatible (cols_A != rows_B)
        A = [[1, 2],
             [3, 4],
             [5, 6]]  # 3 rows, 2 columns
        B = [[7, 8, 9],
             [10, 11, 12]] # 2 rows, 3 columns - This is compatible.
                           # To make it incompatible, change B to have different rows
        B_incompatible = [[7, 8],
                          [9, 10],
                          [11, 12]] # 3 rows, 2 columns

        self.assertIsNone(matrix_multiplication(A, B_incompatible))

    def test_valid_matrix_multiplication(self):
        A = [[1, 2],
             [3, 4]]
        B = [[5, 6],
             [7, 8]]
        expected_result = [[19, 22],
                           [43, 50]]
        self.assertEqual(matrix_multiplication(A, B), expected_result)

        A_rect = [[1, 2, 3],
                  [4, 5, 6]] # 2x3 matrix
        B_rect = [[7, 8],
                  [9, 10],
                  [11, 12]] # 3x2 matrix
        expected_result_rect = [[58, 64],
                                [139, 154]]
        self.assertEqual(matrix_multiplication(A_rect, B_rect), expected_result_rect)

    def test_empty_matrix_inputs(self):
        self.assertIsNone(matrix_multiplication([], []))
        self.assertIsNone(matrix_multiplication([[1, 2]], []))
        self.assertIsNone(matrix_multiplication([], [[1, 2]]))
        self.assertIsNone(matrix_multiplication([[]], [[]])) # Empty inner lists for a 2D matrix
        self.assertIsNone(matrix_multiplication([[]], [[1]])) # Empty A, non-empty B

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)