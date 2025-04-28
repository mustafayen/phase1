# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from my_module import lcm

class TestLCMFunction(unittest.TestCase):

    def test_lcm_of_4_and_6(self):
        result = lcm(4, 6)
        self.assertEqual(result, 12)

    def test_lcm_of_10_and_15(self):
        result = lcm(10, 15)
        self.assertEqual(result, 30)

    def test_lcm_of_7_and_9(self):
        result = lcm(7, 9)
        self.assertEqual(result, 63)

    def test_lcm_of_0_and_5(self):
        result = lcm(0, 5)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()