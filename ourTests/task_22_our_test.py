# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022


import unittest
from task_22_code import gcd

class TestTask22(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(gcd(54, 24), 6)

    def test_case_2(self):
        self.assertEqual(gcd(0, 10), 10)

    def test_case_3(self):
        self.assertEqual(gcd(7, 1), 1)

    def test_case_4(self):
        self.assertEqual(gcd(13, 13), 13)

    def test_case_5(self):
        with self.assertRaises(TypeError):
            gcd("a", "b")

if __name__ == '__main__':
    unittest.main()
