# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022


import unittest
from task_11_code import flatten_list

class TestTask11(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(flatten_list([[1,2],[3,4]]), [1,2,3,4])

    def test_case_2(self):
        self.assertEqual(flatten_list([]), [])

    def test_case_3(self):
        self.assertEqual(flatten_list([[1], [], [2]]), [1,2])

    def test_case_4(self):
        self.assertEqual(flatten_list([[i] for i in range(100)]), list(range(100)))

    def test_case_5(self):
        with self.assertRaises(TypeError):
            flatten_list("not nested")

if __name__ == '__main__':
    unittest.main()
