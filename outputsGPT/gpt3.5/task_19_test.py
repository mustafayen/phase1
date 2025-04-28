# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

class TestBinarySearch(unittest.TestCase):
    
    def test_found_target(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 5
        self.assertEqual(binary_search(arr, target), 4)
        
    def test_not_found_target(self):
        arr = [1, 2, 3, 4, 6, 7, 8, 9, 10]
        target = 5
        self.assertEqual(binary_search(arr, target), -1)
        
    def test_empty_array(self):
        arr = []
        target = 5
        self.assertEqual(binary_search(arr, target), -1)
        
    def test_target_at_first_index(self):
        arr = [5, 10, 15, 20, 25]
        target = 5
        self.assertEqual(binary_search(arr, target), 0)
        
if __name__ == '__main__':
    unittest.main()