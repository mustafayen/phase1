# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022




def zigzag_conversion(s, num_rows):
    if num_rows == 1 or num_rows >= len(s):
        return s
    
    result = ['' for _ in range(num_rows)]
    row = 0
    direction = 1
    
    for char in s:
        result[row] += char
        row += direction
        
        if row == 0 or row == num_rows - 1:
            direction *= -1
        
    return ''.join(result)

# Test the function
s = "PAYPALISHIRING"
num_rows = 3
print(zigzag_conversion(s, num_rows))  # Output: "PAHNAPLSIIGYIR"
