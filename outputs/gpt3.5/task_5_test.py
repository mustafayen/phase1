# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


import unittest

def intersperse(numbers, delimiter):
    return delimiter.join(map(str, numbers))

class TestIntersperse(unittest.TestCase):

    def test_intersperse_with_comma(self):
        numbers = [1, 2, 3, 4, 5]
        delimiter = ","
        result = intersperse(numbers, delimiter)
        self.assertEqual(result, "1,2,3,4,5")

    def test_intersperse_with_dash(self):
        numbers = [10, 20, 30, 40, 50]
        delimiter = "-"
        result = intersperse(numbers, delimiter)
        self.assertEqual(result, "10-20-30-40-50")

    def test_intersperse_with_space(self):
        numbers = [100, 200, 300, 400, 500]
        delimiter = " "
        result = intersperse(numbers, delimiter)
        self.assertEqual(result, "100 200 300 400 500")

if __name__ == '__main__':
    unittest.main()