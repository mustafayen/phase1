# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


import unittest

def filter_integers(values):
    return [val for val in values if isinstance(val, int)]

class TestFilterIntegers(unittest.TestCase):

    def test_filter_integers_only_integers(self):
        values = [1, 2, 3, 'a', 'b', 4.5]
        self.assertEqual(filter_integers(values), [1, 2, 3])

    def test_filter_integers_empty_list(self):
        values = []
        self.assertEqual(filter_integers(values), [])

    def test_filter_integers_no_integers(self):
        values = ['a', 'b', 'c']
        self.assertEqual(filter_integers(values), [])

    def test_filter_integers_mixed_values(self):
        values = [1, 'a', 2, 'b', 3]
        self.assertEqual(filter_integers(values), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()