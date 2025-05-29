# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022


import unittest
from task_17_code import find_pairs_with_sum

class TestTask17(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(find_pairs_with_sum([1, 2, 3, 4], 5), [(1, 4), (2, 3)])

    def test_case_2(self):
        self.assertEqual(find_pairs_with_sum([1, 1, 1], 2), [(1, 1)])

    def test_case_3(self):
        self.assertEqual(find_pairs_with_sum([], 5), [])

    def test_case_4(self):
        self.assertEqual(find_pairs_with_sum([1, 2], 10), [])

    def test_case_5(self):
        self.assertEqual(find_pairs_with_sum([-1, 0, 1, 2], 1), [(-1, 2), (0, 1)])

if __name__ == '__main__':
    unittest.main()
