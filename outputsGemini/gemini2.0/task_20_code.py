def matrix_multiplication(A, B):
    """
    Multiplies two matrices A and B.

    Args:
        A: A 2D list representing the first matrix.
        B: A 2D list representing the second matrix.

    Returns:
        A 2D list representing the product of A and B.
        Returns None if the matrices are not compatible for multiplication.
    """
    if not A or not B or len(A[0]) != len(B):
        return None  # Matrices are not compatible

    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Perform matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):  # or rows_B
                result[i][j] += A[i][k] * B[k][j]
    return result
