# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


import unittest

def rolling_max(numbers):
    if not numbers:
        return []
    
    max_nums = []
    for i in range(len(numbers)):
        max_nums.append(max(numbers[:i+1]))
    
    return max_nums

class TestRollingMax(unittest.TestCase):
    
    def test_empty_list(self):
        self.assertEqual(rolling_max([]), [])
    
    def test_all_positive_numbers(self):
        self.assertEqual(rolling_max([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
    
    def test_all_negative_numbers(self):
        self.assertEqual(rolling_max([-1, -2, -3, -4, -5]), [-1, -1, -1, -1, -1])
    
    def test_mixed_numbers(self):
        self.assertEqual(rolling_max([1, 3, 2, 5, 4]), [1, 3, 3, 5, 5])

if __name__ == '__main__':
    unittest.main()