# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022


import unittest
from task_12_code import remove_duplicates

class TestTask12(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(remove_duplicates([1, 2, 2, 3]), [1, 2, 3])

    def test_case_2(self):
        self.assertEqual(remove_duplicates([]), [])

    def test_case_3(self):
        self.assertEqual(remove_duplicates([1, 1, 1, 1]), [1])

    def test_case_4(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_case_5(self):
        self.assertEqual(remove_duplicates(["a", "b", "a", "c"]), ["a", "b", "c"])

if __name__ == '__main__':
    unittest.main()
