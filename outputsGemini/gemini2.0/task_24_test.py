import unittest
from task_24_code import missing_number # Import the function

class TestMissingNumber(unittest.TestCase):

    def test_missing_number_at_beginning(self):
        """Test when the missing number is 0."""
        self.assertEqual(missing_number([1, 2, 3]), 0)

    def test_missing_number_at_end(self):
        """Test when the missing number is n."""
        self.assertEqual(missing_number([0, 1, 2]), 3)

    def test_missing_number_in_middle(self):
        """Test when the missing number is in the middle."""
        self.assertEqual(missing_number([0, 2, 3]), 1)

    def test_complete_sequence(self):
        """Test when no number is missing."""
        self.assertEqual(missing_number([0, 1, 2, 3]), 4)

    def test_single_element_array(self):
        """Test with a single element array."""
        self.assertEqual(missing_number([0]), 1)
