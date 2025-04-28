import unittest
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

class TestFilterBySubstring(unittest.TestCase):
    def test_substring_present(self):
        strings = ["apple", "banana", "apricot"]
        substring = "app"
        self.assertEqual(filter_by_substring(strings, substring), ["apple", "apricot"])

    def test_substring_not_present(self):
        strings = ["apple", "banana", "cherry"]
        substring = "grape"
        self.assertEqual(filter_by_substring(strings, substring), [])

    def test_empty_string_list(self):
        strings = []
        substring = "test"
        self.assertEqual(filter_by_substring(strings, substring), [])

    def test_empty_substring(self):
        strings = ["apple", "banana"]
        substring = ""
        self.assertEqual(filter_by_substring(strings, substring), ["apple", "banana"])

    def test_substring_at_beginning_and_end(self):
        strings = ["test_start", "middle_test", "test_end"]
        substring = "test"
        self.assertEqual(filter_by_substring(strings, substring), ["test_start", "middle_test", "test_end"])

if __name__ == '__main__':
    unittest.main()
