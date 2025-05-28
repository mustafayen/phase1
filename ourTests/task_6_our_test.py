# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022


import unittest
from task_6_code import sum_even_numbers

class TestTask6(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(sum_even_numbers([1, 2, 3, 4]), 6)

    def test_case_2(self):
        self.assertEqual(sum_even_numbers([1, 3, 5]), 0)

    def test_case_3(self):
        self.assertEqual(sum_even_numbers([]), 0)

    def test_case_4(self):
        self.assertEqual(sum_even_numbers([2]*1000), 2000)

    def test_case_5(self):
        with self.assertRaises(TypeError):
            sum_even_numbers("not a list")

if __name__ == '__main__':
    unittest.main()
