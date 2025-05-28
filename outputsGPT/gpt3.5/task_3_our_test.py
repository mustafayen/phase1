# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022


import unittest
from task_3_code import validate_password

class TestValidatePassword(unittest.TestCase):

    def test_valid_password(self):
        self.assertTrue(validate_password("StrongPass123!"))

    def test_short_password(self):
        self.assertFalse(validate_password("Ab1!"))

    def test_missing_uppercase(self):
        self.assertFalse(validate_password("weakpass1!"))

    def test_missing_digit(self):
        self.assertFalse(validate_password("NoDigitsHere!"))

    def test_missing_special_char(self):
        self.assertFalse(validate_password("NoSpecial123"))

    def test_empty_string(self):
        self.assertFalse(validate_password(""))

if __name__ == '__main__':
    unittest.main()
