# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022




def check_brackets(string):
    stack = []
    brackets = {'(': ')', '[': ']', '{': '}'}
    
    for char in string:
        if char in brackets.keys():
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False
    
    return len(stack) == 0

# Test the function
print(check_brackets("()"))  # True
print(check_brackets("()[]{}"))  # True
print(check_brackets("(]"))  # False
print(check_brackets("([)]"))  # False

