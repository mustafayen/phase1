# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022


import unittest
from task_7_code import count_vowels

class TestTask7(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(count_vowels("hello"), 2)

    def test_case_2(self):
        self.assertEqual(count_vowels(""), 0)

    def test_case_3(self):
        self.assertEqual(count_vowels("bcdfgh"), 0)

    def test_case_4(self):
        self.assertEqual(count_vowels("AEIOUaeiou"), 10)

    def test_case_5(self):
        self.assertEqual(count_vowels("Python Programming"), 4)

if __name__ == '__main__':
    unittest.main()
