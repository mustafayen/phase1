# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest

def find_pairs_with_sum(numbers, target):
    pairs = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                pairs.append((numbers[i], numbers[j]))
    return pairs

class TestFindPairsWithSum(unittest.TestCase):

    def test_find_pairs_with_sum(self):
        self.assertEqual(find_pairs_with_sum([1, 2, 3, 4, 5], 5), [(1, 4), (2, 3)])
        self.assertEqual(find_pairs_with_sum([1, 2, 3, 4, 5], 10), [])
        self.assertEqual(find_pairs_with_sum([1, 2, 3, 4, 5], 6), [(1, 5), (2, 4)])
    
    def test_find_pairs_with_sum_empty_list(self):
        self.assertEqual(find_pairs_with_sum([], 5), [])
    
    def test_find_pairs_with_sum_negative_numbers(self):
        self.assertEqual(find_pairs_with_sum([-1, 2, -3, 4, 5], 1), [(-1, 2), (-3, 4)])

if __name__ == '__main__':
    unittest.main()