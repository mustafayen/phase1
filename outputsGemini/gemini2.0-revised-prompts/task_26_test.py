import unittest
from task_26_code import most_frequent_element # Import the function

class TestMostFrequentElement(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(most_frequent_element([]))

    def test_single_element(self):
        self.assertEqual(most_frequent_element([1]), 1)

    def test_unique_elements(self):
        self.assertEqual(most_frequent_element([1, 2, 3, 4, 5]), 1)

    def test_multiple_occurrences(self):
        self.assertEqual(most_frequent_element([1, 2, 2, 3, 3, 3, 4]), 3)

    def test_tie_for_most_frequent(self):
        # Corrected test case: 1 appears first with frequency 2, 2 appears second with frequency 2.
        # The expected result should be 1.
        self.assertEqual(most_frequent_element([1, 2, 2, 1, 3, 3]), 1)
        # Another test for tie-breaking
        self.assertEqual(most_frequent_element([5, 5, 1, 1, 2]), 5)
        self.assertEqual(most_frequent_element([10, 20, 10, 20, 30]), 10)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)