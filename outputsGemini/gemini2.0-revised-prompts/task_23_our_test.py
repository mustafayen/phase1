# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022


import unittest
from task_23_code import lcm

class TestTask23(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(lcm(4, 6), 12)

    def test_case_2(self):
        self.assertEqual(lcm(0, 5), 0)

    def test_case_3(self):
        self.assertEqual(lcm(7, 1), 7)

    def test_case_4(self):
        self.assertEqual(lcm(13, 13), 13)

    def test_case_5(self):
        self.assertEqual(lcm(21, 6), 42)

if __name__ == '__main__':
    unittest.main()
