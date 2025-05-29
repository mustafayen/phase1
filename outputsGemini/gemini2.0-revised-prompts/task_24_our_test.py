# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022


import unittest
from task_24_code import missing_number

class TestTask24(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(missing_number([3, 0, 1]), 2)

    def test_case_2(self):
        self.assertEqual(missing_number([0, 1]), 2)

    def test_case_3(self):
        self.assertEqual(missing_number([9,6,4,2,3,5,7,0,1]), 8)

    def test_case_4(self):
        self.assertEqual(missing_number([0]), 1)

    def test_case_5(self):
        self.assertEqual(missing_number([1]), 0)

if __name__ == '__main__':
    unittest.main()
