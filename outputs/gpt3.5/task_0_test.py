# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


import unittest

def has_close_elements(numbers, threshold):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if abs(numbers[i] - numbers[j]) <= threshold:
                return True
    return False

class TestHasCloseElements(unittest.TestCase):

    def test_close_elements_within_threshold(self):
        self.assertTrue(has_close_elements([1, 2, 3, 4, 5], 2))

    def test_close_elements_outside_threshold(self):
        self.assertFalse(has_close_elements([1, 2, 3, 4, 5], 1))

    def test_empty_list(self):
        self.assertFalse(has_close_elements([], 2))

    def test_single_element_list(self):
        self.assertFalse(has_close_elements([1], 2))

if __name__ == '__main__':
    unittest.main()