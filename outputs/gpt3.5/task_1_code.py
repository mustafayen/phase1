# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


```python
def separate_paren_groups(paren_string):
    stack = []
    result = []
    current_group = ""
    
    for char in paren_string:
        if char == "(":
            if current_group:
                stack.append(current_group)
                current_group = ""
            stack.append("(")
        elif char == ")":
            if current_group:
                stack.append(current_group)
                current_group = ""
            temp_group = ""
            while stack[-1] != "(":
                temp_group = stack.pop() + temp_group
            stack.pop()  # Remove the "("
            stack.append(temp_group)
        else:
            current_group += char
    
    if current_group:
        stack.append(current_group)
    
    return stack

# Example usage
paren_string = "abc(def)ghi(jkl)mno"
result = separate_paren_groups(paren_string)
print(result)
```

#This function takes a string `paren_string` as input and separates the groups enclosed in parentheses. It uses a stack to keep track of the groups and builds the groups based on the parentheses. The function returns a list of separated groups.