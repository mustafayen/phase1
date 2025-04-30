# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022


def validate_password(password):
    if len(password) < 8:
        return False
    
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
    
    return has_uppercase and has_lowercase and has_digit

# Test the function
print(validate_password("Password123"))  # True
print(validate_password("password"))     # False
print(validate_password("12345678"))     # False
print(validate_password("Pass123"))      # False
