# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022


import unittest
from task_10_code import anagram_check

class TestTask10(unittest.TestCase):

    def test_case_1(self):
        self.assertTrue(anagram_check("listen", "silent"))

    def test_case_2(self):
        self.assertFalse(anagram_check("hello", "world"))

    def test_case_3(self):
        self.assertTrue(anagram_check("", ""))

    def test_case_4(self):
        self.assertTrue(anagram_check("aabbcc", "baccab"))

    def test_case_5(self):
        with self.assertRaises(AttributeError):
            anagram_check(123, "321")

if __name__ == '__main__':
    unittest.main()
