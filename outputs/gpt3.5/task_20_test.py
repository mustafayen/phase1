# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


import unittest

def find_closest_elements(numbers):
    numbers.sort()
    min_diff = float('inf')
    closest_elements = []
    
    for i in range(len(numbers)-1):
        diff = abs(numbers[i] - numbers[i+1])
        if diff < min_diff:
            min_diff = diff
            closest_elements = [numbers[i], numbers[i+1]]
    
    return closest_elements

class TestFindClosestElements(unittest.TestCase):
    
    def test_two_elements(self):
        self.assertEqual(find_closest_elements([1, 2]), [1, 2])
    
    def test_multiple_elements(self):
        self.assertEqual(find_closest_elements([1, 5, 3, 8, 6]), [5, 6])
    
    def test_negative_numbers(self):
        self.assertEqual(find_closest_elements([-10, -5, -3, -8, -6]), [-6, -5])
    
    def test_duplicate_elements(self):
        self.assertEqual(find_closest_elements([1, 2, 2, 3, 4]), [2, 2])

if __name__ == '__main__':
    unittest.main()