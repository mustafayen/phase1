# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_8_code import rotate_matrix

class TestTask8(unittest.TestCase):

    def test_case_1(self):
        matrix = [[1, 2], [3, 4]]
        rotate_matrix(matrix)
        self.assertEqual(matrix, [[3, 1], [4, 2]])

    def test_case_2(self):
        matrix = [[1]]
        rotate_matrix(matrix)
        self.assertEqual(matrix, [[1]])

    def test_case_3(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        rotate_matrix(matrix)
        self.assertEqual(matrix, [[7, 4, 1], [8, 5, 2], [9, 6, 3]])

    def test_case_4(self):
        matrix = []
        rotate_matrix(matrix)
        self.assertEqual(matrix, [])

    def test_case_5(self):
        matrix = [[1, 2], [3, 4], [5, 6]]
        with self.assertRaises(IndexError):
            rotate_matrix(matrix)

if __name__ == '__main__':
    unittest.main()
