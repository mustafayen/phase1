# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



def convert_to_zigzag(s, num_rows):
    if num_rows == 1:
        return s
    
    rows = ['' for _ in range(num_rows)]
    index = 0
    direction = 1
    
    for char in s:
        rows[index] += char
        index += direction
        
        if index == 0 or index == num_rows - 1:
            direction *= -1
    
    return ''.join(rows)
    
# Example usage
s = "PAYPALISHIRING"
num_rows = 3
print(convert_to_zigzag(s, num_rows))  # Output: "PAHNAPLSIIGYIR"
