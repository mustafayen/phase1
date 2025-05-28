# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_3_code import validate_password

class TestCheckPasswordCriteria(unittest.TestCase):

    def test_valid_password(self):
        self.assertTrue(validate_password("Password123!"))

    def test_too_short_password(self):
        self.assertFalse(validate_password("Pass1!"))

    def test_no_uppercase_letter(self):
        self.assertFalse(validate_password("password123!"))

    def test_no_digit(self):
        self.assertFalse(validate_password("Password!"))

    def test_no_special_character(self):
        self.assertFalse(validate_password("Password123"))

if __name__ == '__main__':
    unittest.main()
