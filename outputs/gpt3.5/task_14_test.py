# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


import unittest

def all_prefixes(string):
    prefixes = [string[:i] for i in range(1, len(string)+1)]
    return prefixes

class TestAllPrefixes(unittest.TestCase):

    def test_all_prefixes_empty_string(self):
        self.assertEqual(all_prefixes(''), [])

    def test_all_prefixes_single_character_string(self):
        self.assertEqual(all_prefixes('a'), ['a'])

    def test_all_prefixes_multiple_character_string(self):
        self.assertEqual(all_prefixes('hello'), ['h', 'he', 'hel', 'hell', 'hello'])

    def test_all_prefixes_special_characters(self):
        self.assertEqual(all_prefixes('@#$%'), ['@', '@#', '@#$', '@#$%'])

if __name__ == '__main__':
    unittest.main()