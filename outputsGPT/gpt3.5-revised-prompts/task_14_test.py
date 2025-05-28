# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_14_code import find_median

class TestFindMedian(unittest.TestCase):

    def test_odd_number_of_elements(self):
        self.assertEqual(find_median([1, 2, 3, 4, 5]), 3)

    def test_even_number_of_elements(self):
        self.assertEqual(find_median([1, 2, 3, 4]), 2.5)

    def test_negative_numbers(self):
        self.assertEqual(find_median([-5, -3, 0, 2, 4]), 0)

    def test_float_numbers(self):
        self.assertEqual(find_median([1.5, 2.5, 3.5, 4.5]), 3)

if __name__ == '__main__':
    unittest.main()
