import unittest
import math

from task_0_code import calculate_area  

class TestCalculateArea(unittest.TestCase):

    def test_positive_radius(self):
        """Test with a positive radius."""
        radius = 5
        expected_area = math.pi * radius**2
        self.assertAlmostEqual(calculate_area(radius), expected_area, places=7)

    def test_zero_radius(self):
        """Test with a zero radius."""
        radius = 0
        expected_area = 0
        self.assertEqual(calculate_area(radius), expected_area)

    def test_negative_radius(self):
        """Test with a negative radius."""
        radius = -3
        expected_area = 0  # Function should return 0 for negative radius
        self.assertEqual(calculate_area(radius), expected_area)

    def test_large_radius(self):
        """Test with a large radius."""
        radius = 1000
        expected_area = math.pi * radius**2
        self.assertAlmostEqual(calculate_area(radius), expected_area, places=7)

    def test_decimal_radius(self):
        """Test with a decimal radius."""
        radius = 2.5
        expected_area = math.pi * radius**2
        self.assertAlmostEqual(calculate_area(radius), expected_area, places=7)

if __name__ == '__main__':  # pragma: no cover
    unittest.main()
