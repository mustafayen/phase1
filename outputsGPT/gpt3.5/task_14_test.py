# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_14_code import calculate_median

class TestCalculateMedian(unittest.TestCase):

    def test_calculate_median_odd_numbers(self):
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual(calculate_median(numbers), 3)

    def test_calculate_median_even_numbers(self):
        numbers = [1, 2, 3, 4]
        self.assertEqual(calculate_median(numbers), 2.5)

    def test_calculate_median_empty_list(self):
        numbers = []
        self.assertIsNone(calculate_median(numbers))

    def test_calculate_median_single_number(self):
        numbers = [5]
        self.assertEqual(calculate_median(numbers), 5)

if __name__ == '__main__':  # pragma: no cover
    unittest.main()