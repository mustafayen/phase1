# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


import unittest

def below_zero(operations):
    count = 0
    for num in operations:
        if num < 0:
            count += 1
    return count

class TestBelowZero(unittest.TestCase):
    
    def test_all_negative_numbers(self):
        self.assertEqual(below_zero([-1, -2, -3, -4]), 4)
    
    def test_mixed_numbers(self):
        self.assertEqual(below_zero([-1, 2, -3, 4]), 2)
    
    def test_no_negative_numbers(self):
        self.assertEqual(below_zero([1, 2, 3, 4]), 0)
    
    def test_empty_list(self):
        self.assertEqual(below_zero([]), 0)

if __name__ == '__main__':
    unittest.main()