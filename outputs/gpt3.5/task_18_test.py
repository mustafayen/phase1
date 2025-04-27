# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


import unittest

def how_many_times(string, substring):
    count = 0
    start = 0
    while start < len(string):
        index = string.find(substring, start)
        if index != -1:
            count += 1
            start = index + 1
        else:
            break
    return count

class TestHowManyTimes(unittest.TestCase):

    def test_one_occurrence(self):
        result = how_many_times("hello world", "world")
        self.assertEqual(result, 1)

    def test_multiple_occurrences(self):
        result = how_many_times("hello hello hello", "hello")
        self.assertEqual(result, 3)

    def test_no_occurrence(self):
        result = how_many_times("python unittest", "hello")
        self.assertEqual(result, 0)

    def test_empty_string(self):
        result = how_many_times("", "hello")
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()