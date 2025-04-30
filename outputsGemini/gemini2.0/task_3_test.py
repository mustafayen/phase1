import unittest
from task_3_code import validate_password # Import the function

class TestValidatePassword(unittest.TestCase):

    def test_valid_password(self):
        """Test with a valid password."""
        password = "Password123"
        self.assertTrue(validate_password(password))

    def test_short_password(self):
        """Test with a password shorter than 8 characters."""
        password = "Pass12"
        self.assertFalse(validate_password(password))

    def test_missing_uppercase(self):
        """Test with a password missing an uppercase letter."""
        password = "password123"
        self.assertFalse(validate_password(password))

    def test_missing_lowercase(self):
        """Test with a password missing a lowercase letter."""
        password = "PASSWORD123"
        self.assertFalse(validate_password(password))

    def test_missing_digit(self):
        """Test with a password missing a digit."""
        password = "PasswordABC"
        self.assertFalse(validate_password(password))
