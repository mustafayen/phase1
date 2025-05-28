# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022


import unittest
from task_19_code import binary_search

class TestTask19(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)

    def test_case_2(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 6), -1)

    def test_case_3(self):
        self.assertEqual(binary_search([], 3), -1)

    def test_case_4(self):
        self.assertEqual(binary_search([3], 3), 0)

    def test_case_5(self):
        self.assertEqual(binary_search([1, 3, 5, 7, 9], 7), 3)

if __name__ == '__main__':
    unittest.main()
