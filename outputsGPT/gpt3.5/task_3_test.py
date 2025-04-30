# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_3_code import validate_password

class TestValidatePassword(unittest.TestCase):

    def test_valid_password(self):
        self.assertTrue(validate_password("Abcdefg1!"))

    def test_invalid_password_too_short(self):
        self.assertFalse(validate_password("Abc1!"))

    def test_invalid_password_no_special_character(self):
        self.assertFalse(validate_password("Abcdefg1"))

    def test_invalid_password_no_number(self):
        self.assertFalse(validate_password("Abcdefg!"))

if __name__ == '__main__':
    unittest.main()