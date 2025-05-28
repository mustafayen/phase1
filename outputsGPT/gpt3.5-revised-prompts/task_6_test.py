# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_6_code import sum_even_numbers

class TestSumEvenNumbers(unittest.TestCase):

    def test_sum_even_numbers(self):
        self.assertEqual(sum_even_numbers([1, 2, 3, 4, 5]), 6)

    def test_sum_even_numbers_empty_list(self):
        self.assertEqual(sum_even_numbers([]), 0)

    def test_sum_even_numbers_all_odd_numbers(self):
        self.assertEqual(sum_even_numbers([1, 3, 5]), 0)

    def test_sum_even_numbers_all_even_numbers(self):
        self.assertEqual(sum_even_numbers([2, 4, 6]), 12)

if __name__ == '__main__':
    unittest.main()