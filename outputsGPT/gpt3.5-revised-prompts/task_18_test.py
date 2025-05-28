# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_18_code import group_anagrams

class TestGroupAnagrams(unittest.TestCase):

    def test_group_anagrams_empty_input(self):
        self.assertEqual(group_anagrams([]), [])

    def test_group_anagrams_single_anagram(self):
        self.assertEqual(group_anagrams(['listen', 'silent']), [['listen', 'silent']])

    def test_group_anagrams_multiple_anagrams(self):
        self.assertEqual(group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']), [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])

    def test_group_anagrams_no_anagrams(self):
        self.assertEqual(group_anagrams(['hello', 'world', 'python']), [['hello'], ['world'], ['python']])

if __name__ == '__main__':
    unittest.main()