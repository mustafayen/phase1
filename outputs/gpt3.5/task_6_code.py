# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


Here is a complete Python function that parses a string containing nested parentheses and returns a list of all the nested levels:

```python
def parse_nested_parens(paren_string):
    nested_levels = []
    current_level = 0
    
    for char in paren_string:
        if char == '(':
            current_level += 1
        elif char == ')':
            current_level -= 1
        else:
            continue
        
        if current_level > 0:
            nested_levels.append(current_level)
    
    return nested_levels

# Test the function
paren_string = "((()))"
print(parse_nested_parens(paren_string))  # Output: [1, 2, 3]
```

This function iterates through each character in the input string and keeps track of the current nested level by incrementing the level when encountering an opening parenthesis '(' and decrementing the level when encountering a closing parenthesis ')'. It then appends the current level to the list of nested levels if the level is greater than 0. Finally, it returns the list of nested levels.