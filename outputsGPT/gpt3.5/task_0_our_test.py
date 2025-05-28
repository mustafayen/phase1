# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022


import unittest
from task_0_code import calculate_area

class TestCalculateArea(unittest.TestCase):

    def test_regular_case(self):
        self.assertAlmostEqual(calculate_area(3), 28.2743, places=4)

    def test_zero_radius(self):
        self.assertEqual(calculate_area(0), 0)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_area(-5)

    def test_large_radius(self):
        self.assertAlmostEqual(calculate_area(100), 31415.9265, places=4)

    def test_float_radius(self):
        self.assertAlmostEqual(calculate_area(1.5), 7.0686, places=4)

if __name__ == '__main__':
    unittest.main()
