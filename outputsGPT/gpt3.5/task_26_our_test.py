# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022


import unittest
from task_26_code import most_frequent_element

class TestTask26(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(most_frequent_element([1, 2, 2, 3]), 2)

    def test_case_2(self):
        self.assertEqual(most_frequent_element([1]), 1)

    def test_case_3(self):
        self.assertEqual(most_frequent_element([1, 1, 2, 2]), 1)  # first seen

    def test_case_4(self):
        self.assertEqual(most_frequent_element(["a", "b", "a", "c", "a"]), "a")

    def test_case_5(self):
        self.assertEqual(most_frequent_element([]), None)

if __name__ == '__main__':
    unittest.main()
