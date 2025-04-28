# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest

def most_frequent_element(lst):
    if len(lst) == 0:
        return None
    else:
        return max(set(lst), key=lst.count)

class TestMostFrequentElement(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(most_frequent_element([]))

    def test_single_element_list(self):
        self.assertEqual(most_frequent_element([1]), 1)

    def test_multiple_elements_list(self):
        self.assertEqual(most_frequent_element([1, 2, 2, 3, 3, 3]), 3)

    def test_duplicate_most_frequent_element(self):
        self.assertEqual(most_frequent_element([1, 1, 2, 2, 3, 3]), 1)

if __name__ == '__main__':
    unittest.main()