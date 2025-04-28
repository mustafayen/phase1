# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest

def get_unique_elements(lst):
    return list(set(lst))

class TestGetUniqueElements(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(get_unique_elements([]), [])

    def test_all_unique_elements(self):
        self.assertEqual(get_unique_elements([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_duplicate_elements(self):
        self.assertEqual(get_unique_elements([1, 2, 2, 3, 3, 4]), [1, 2, 3, 4])

    def test_mixed_elements(self):
        self.assertEqual(get_unique_elements([1, 2, 3, 3, 4, 4, 5]), [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()