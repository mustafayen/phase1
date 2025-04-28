# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest

def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        return (numbers[n//2 - 1] + numbers[n//2]) / 2
    else:
        return numbers[n//2]

class TestCalculateMedian(unittest.TestCase):

    def test_odd_number_of_elements(self):
        self.assertEqual(calculate_median([1, 2, 3, 4, 5]), 3)

    def test_even_number_of_elements(self):
        self.assertEqual(calculate_median([1, 2, 3, 4]), 2.5)

    def test_negative_numbers(self):
        self.assertEqual(calculate_median([-5, -3, -1, 1, 3, 5]), 0)

    def test_duplicate_numbers(self):
        self.assertEqual(calculate_median([1, 2, 2, 3, 4]), 2)

if __name__ == '__main__':
    unittest.main()