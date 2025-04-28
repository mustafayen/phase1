# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



The function `rotate_matrix` takes a matrix as input and rotates it 90 degrees clockwise.

Here is the implementation of the function:

```python
def rotate_matrix(matrix):
    n = len(matrix)
    
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]
    
    return matrix

# Test the function
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rotated_matrix = rotate_matrix(matrix)
for row in rotated_matrix:
    print(row)
```

This function first transposes the matrix by swapping the elements across the diagonal, then reverses each row to rotate the matrix 90 degrees clockwise.