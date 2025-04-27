# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


import unittest

def truncate_number(number):
    return int(number)

class TestTruncateNumber(unittest.TestCase):

    def test_truncate_positive_number(self):
        self.assertEqual(truncate_number(10.5), 10)

    def test_truncate_negative_number(self):
        self.assertEqual(truncate_number(-5.8), -5)

    def test_truncate_zero(self):
        self.assertEqual(truncate_number(0), 0)

    def test_truncate_large_number(self):
        self.assertEqual(truncate_number(1000000.9), 1000000)

if __name__ == '__main__':
    unittest.main()