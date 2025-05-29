# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_9_code import reverse_string

class TestTask9(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_case_2(self):
        self.assertEqual(reverse_string(""), "")

    def test_case_3(self):
        self.assertEqual(reverse_string("a"), "a")

    def test_case_4(self):
        self.assertEqual(reverse_string("racecar"), "racecar")

    def test_case_5(self):
        with self.assertRaises(TypeError):
            reverse_string(12345)

    def test_case_6(self):
        self.assertEqual(reverse_string("xy"), "yx")

if __name__ == '__main__':
    unittest.main()
