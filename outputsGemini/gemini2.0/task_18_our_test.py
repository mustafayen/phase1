# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_18_code import group_anagrams

class TestTask18(unittest.TestCase):

    def test_case_1(self):
        result = group_anagrams(["bat", "tab", "tap", "pat"])
        self.assertTrue(["bat", "tab"] in result)
        self.assertTrue(["tap", "pat"] in result)

    def test_case_2(self):
        self.assertEqual(group_anagrams([]), [])

    def test_case_3(self):
        self.assertEqual(group_anagrams(["abc"]), [["abc"]])

    def test_case_4(self):
        result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        lengths = sorted([sorted(g) for g in result])
        expected = sorted([sorted(g) for g in [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]])
        self.assertEqual(lengths, expected)

    def test_case_5(self):
        self.assertEqual(group_anagrams([""]), [[""]])

if __name__ == '__main__':
    unittest.main()
