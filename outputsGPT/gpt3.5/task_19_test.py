# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_19_code import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_binary_search_found(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 5
        self.assertEqual(binary_search(arr, target), 4)

    def test_binary_search_not_found(self):
        arr = [1, 2, 3, 4, 6, 7, 8, 9, 10]
        target = 5
        self.assertEqual(binary_search(arr, target), -1)

    def test_binary_search_empty_array(self):
        arr = []
        target = 5
        self.assertEqual(binary_search(arr, target), -1)

    def test_binary_search_single_element_array(self):
        arr = [5]
        target = 5
        self.assertEqual(binary_search(arr, target), 0)

if __name__ == '__main__':
    unittest.main()