# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_23_code import lcm

class TestLCMFunction(unittest.TestCase):

    def test_lcm_positive_numbers(self):
        result = lcm(4, 6)
        self.assertEqual(result, 12)

    def test_lcm_negative_numbers(self):
        result = lcm(-8, -12)
        self.assertEqual(result, 24)

    def test_lcm_zero(self):
        result = lcm(0, 5)
        self.assertEqual(result, 0)

    def test_lcm_same_number(self):
        result = lcm(7, 7)
        self.assertEqual(result, 7)

if __name__ == '__main__':
    unittest.main()