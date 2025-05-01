# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_13_code import get_unique_elements

class TestGetUniqueElements(unittest.TestCase):

    def test_all_unique_elements(self):
        lst = [1, 2, 3, 4, 5]
        self.assertEqual(get_unique_elements(lst), [1, 2, 3, 4, 5])

    def test_duplicate_elements(self):
        lst = [1, 2, 2, 3, 3, 4, 5]
        self.assertEqual(get_unique_elements(lst), [1, 2, 3, 4, 5])

    def test_empty_list(self):
        lst = []
        self.assertEqual(get_unique_elements(lst), [])

    def test_mixed_elements(self):
        lst = [1, 'a', 2, 'b', 3]
        self.assertEqual(get_unique_elements(lst), [1, 'a', 2, 'b', 3])

if __name__ == '__main__':  # pragma: no cover
    unittest.main()