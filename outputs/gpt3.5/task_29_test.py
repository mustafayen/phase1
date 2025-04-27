# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


import unittest

def filter_by_prefix(strings, prefix):
    return [s for s in strings if s.startswith(prefix)]

class TestFilterByPrefix(unittest.TestCase):

    def test_filter_by_prefix_empty_list(self):
        self.assertEqual(filter_by_prefix([], 'prefix'), [])

    def test_filter_by_prefix_no_match(self):
        strings = ['apple', 'banana', 'cherry']
        self.assertEqual(filter_by_prefix(strings, 'grape'), [])

    def test_filter_by_prefix_single_match(self):
        strings = ['apple', 'banana', 'cherry']
        self.assertEqual(filter_by_prefix(strings, 'b'), ['banana'])

    def test_filter_by_prefix_multiple_matches(self):
        strings = ['apple', 'banana', 'cherry', 'blueberry']
        self.assertEqual(filter_by_prefix(strings, 'b'), ['banana', 'blueberry'])

if __name__ == '__main__':
    unittest.main()