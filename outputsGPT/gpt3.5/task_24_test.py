# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest

def missing_number(nums):
    n = len(nums)
    total_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return total_sum - actual_sum

class TestMissingNumber(unittest.TestCase):

    def test_missing_number_1(self):
        self.assertEqual(missing_number([3, 0, 1]), 2)

    def test_missing_number_2(self):
        self.assertEqual(missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)

    def test_missing_number_3(self):
        self.assertEqual(missing_number([1, 2, 3, 4, 5, 6, 7, 8, 9]), 0)

    def test_missing_number_4(self):
        self.assertEqual(missing_number([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 11)

if __name__ == '__main__':
    unittest.main()