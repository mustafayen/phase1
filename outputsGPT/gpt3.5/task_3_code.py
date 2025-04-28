# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



The function `validate_password` should take a password as input and return True if the password meets the following criteria:

1. The password must be at least 8 characters long.
2. The password must contain at least one uppercase letter.
3. The password must contain at least one lowercase letter.
4. The password must contain at least one digit.

If the password meets all of these criteria, the function should return True. Otherwise, it should return False.

Here is the implementation of the `validate_password` function:

```python
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
```

You can test the function with different passwords to see if it correctly validates them based on the criteria mentioned above.