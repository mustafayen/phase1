# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_0_code import calculate_area

class TestCalculateArea(unittest.TestCase):

    def test_positive_radius(self):
        self.assertEqual(calculate_area(5), 78.54)

    def test_negative_radius(self):
        self.assertEqual(calculate_area(-3), 0)

    def test_zero_radius(self):
        self.assertEqual(calculate_area(0), 0)

    def test_large_radius(self):
        self.assertAlmostEqual(calculate_area(100), 31415.93, places=2)

if __name__ == '__main__':  # pragma: no cover
    unittest.main()