def rotate_matrix(matrix):
    """
    Rotates a square matrix 90 degrees clockwise.
    The function modifies the matrix in place.

    Args:
        matrix: A square matrix represented as a list of lists.

    Returns:
        None. The matrix is modified in place.
    """
    n = len(matrix)
    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row
    for row in matrix:
        row.reverse()
