# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_0_code import calculate_circle_area

class TestCalculateCircleArea(unittest.TestCase):

    def test_area_with_radius_0(self):
        self.assertAlmostEqual(calculate_circle_area(0), 0.0)

    def test_area_with_radius_1(self):
        self.assertAlmostEqual(calculate_circle_area(1), 3.141592653589793)

    def test_area_with_radius_5(self):
        self.assertAlmostEqual(calculate_circle_area(5), 78.53981633974483)

    def test_area_with_large_radius(self):
        self.assertAlmostEqual(calculate_circle_area(100), 31415.926535897932)

if __name__ == '__main__':
    unittest.main()
