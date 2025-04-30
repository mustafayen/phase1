# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_26_code import most_frequent_element

class TestMostFrequentElement(unittest.TestCase):

    def test_most_frequent_element(self):
        self.assertEqual(most_frequent_element([1, 2, 2, 3, 3, 3]), 3)

    def test_most_frequent_element_empty_list(self):
        self.assertEqual(most_frequent_element([]), None)

    def test_most_frequent_element_single_element(self):
        self.assertEqual(most_frequent_element([5]), 5)

    def test_most_frequent_element_multiple_most_frequent_elements(self):
        self.assertEqual(most_frequent_element([1, 1, 2, 2, 3, 3]), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()