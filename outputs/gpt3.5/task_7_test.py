# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


import unittest

def filter_by_substring(strings, substring):
    return [string for string in strings if substring in string]

class TestFilterBySubstring(unittest.TestCase):

    def test_filter_by_substring_empty_list(self):
        strings = []
        substring = "abc"
        self.assertEqual(filter_by_substring(strings, substring), [])

    def test_filter_by_substring_no_matching_strings(self):
        strings = ["def", "ghi", "jkl"]
        substring = "abc"
        self.assertEqual(filter_by_substring(strings, substring), [])

    def test_filter_by_substring_one_matching_string(self):
        strings = ["abcdef"]
        substring = "abc"
        self.assertEqual(filter_by_substring(strings, substring), ["abcdef"])

    def test_filter_by_substring_multiple_matching_strings(self):
        strings = ["abc", "defabc", "ghiabc"]
        substring = "abc"
        self.assertEqual(filter_by_substring(strings, substring), ["abc", "defabc", "ghiabc"])

if __name__ == '__main__':
    unittest.main()