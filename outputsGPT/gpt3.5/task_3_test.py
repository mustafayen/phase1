# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest

def validate_password(password):
    # Check if password is at least 8 characters long
    if len(password) < 8:
        return False
    # Check if password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False
    # Check if password contains at least one lowercase letter
    if not any(char.islower() for char in password):
        return False
    # Check if password contains at least one digit
    if not any(char.isdigit() for char in password):
        return False
    return True

class TestValidatePassword(unittest.TestCase):

    def test_too_short_password(self):
        self.assertFalse(validate_password("abc123"))

    def test_no_uppercase_letter(self):
        self.assertFalse(validate_password("abcdefg1"))

    def test_no_lowercase_letter(self):
        self.assertFalse(validate_password("ABCDEFG1"))

    def test_no_digit(self):
        self.assertFalse(validate_password("Abcdefg"))

    def test_valid_password(self):
        self.assertTrue(validate_password("Abcdefg1"))

if __name__ == '__main__':
    unittest.main()