# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



The function `zigzag_conversion` takes in a string `s` and an integer `num_rows` and returns the zigzag conversion of the string based on the number of rows specified.

Here is the implementation of the function:

```python
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
```

In this function, we create a list `result` to store the characters in each row of the zigzag pattern. We iterate through the input string `s` and append each character to the corresponding row in the `result` list. We also keep track of the current row and the direction in which we are moving (up or down). Finally, we join all the rows together to get the zigzag conversion of the input string.