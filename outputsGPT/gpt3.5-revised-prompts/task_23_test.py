# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_23_code import lcm

class TestLCMFunction(unittest.TestCase):

    def test_lcm_of_3_and_5(self):
        self.assertEqual(lcm(3, 5), 15)

    def test_lcm_of_0_and_7(self):
        self.assertEqual(lcm(0, 7), 0)

    def test_lcm_of_10_and_15(self):
        self.assertEqual(lcm(10, 15), 30)

    def test_lcm_of_12_and_18(self):
        self.assertEqual(lcm(12, 18), 36)

    def test_lcm_of_0_and_0(self):
        self.assertEqual(lcm(0, 0), 0)

if __name__ == '__main__':
    unittest.main()