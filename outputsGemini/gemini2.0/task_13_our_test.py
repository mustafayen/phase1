# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_13_code import get_unique_elements

class TestTask13(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(get_unique_elements([1, 2, 2, 3]), [1, 2, 3])

    def test_case_2(self):
        self.assertEqual(get_unique_elements([1, 1, 1, 1]), [1])

    def test_case_3(self):
        self.assertEqual(get_unique_elements([]), [])

    def test_case_4(self):
        self.assertEqual(get_unique_elements([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_case_5(self):
        self.assertEqual(get_unique_elements(["a", "b", "a", "c"]), ["a", "b", "c"])

if __name__ == '__main__':
    unittest.main()
