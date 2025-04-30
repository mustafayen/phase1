# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_18_code import group_anagrams

class TestGroupAnagrams(unittest.TestCase):

    def test_empty_input(self):
        self.assertEqual(group_anagrams([]), [])

    def test_single_anagram(self):
        self.assertEqual(group_anagrams(['listen', 'silent']), [['listen', 'silent']])

    def test_multiple_anagrams(self):
        self.assertEqual(group_anagrams(['listen', 'silent', 'hello', 'olelh']), [['listen', 'silent'], ['hello', 'olelh']])

    def test_no_anagrams(self):
        self.assertEqual(group_anagrams(['listen', 'hello', 'world']), [['listen'], ['hello'], ['world']])

if __name__ == '__main__':
    unittest.main()