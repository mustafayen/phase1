# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022




import re

def validate_password(password):
    if len(password) < 8:
        return False
    
    if not re.search("[A-Z]", password):
        return False
    
    if not re.search("[a-z]", password):
        return False
    
    if not re.search("[0-9]", password):
        return False
    
    if not re.search("[!@#$%^&*]", password):
        return False
    
    return True

# Test the function
print(validate_password("Abcdefg1@"))  # True
print(validate_password("password123"))  # False
print(validate_password("ABCD1234"))  # False
print(validate_password("abcdefg!"))  # False

