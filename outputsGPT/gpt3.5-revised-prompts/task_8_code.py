# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



def rotate_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    rotated_matrix = [[0 for _ in range(rows)] for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            rotated_matrix[j][rows-1-i] = matrix[i][j]
    
    return rotated_matrix

# Example
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rotated = rotate_matrix(matrix)
for row in rotated:
    print(row)
