# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


import unittest

def mean_absolute_deviation(numbers):
    mean = sum(numbers) / len(numbers)
    deviations = [abs(num - mean) for num in numbers]
    return sum(deviations) / len(deviations)

class TestMeanAbsoluteDeviation(unittest.TestCase):

    def test_all_positive_numbers(self):
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual(mean_absolute_deviation(numbers), 1.2)

    def test_mixed_positive_and_negative_numbers(self):
        numbers = [-3, 0, 2, 5, -1]
        self.assertEqual(mean_absolute_deviation(numbers), 2.4)

    def test_all_negative_numbers(self):
        numbers = [-5, -4, -3, -2, -1]
        self.assertEqual(mean_absolute_deviation(numbers), 1.2)

    def test_empty_list(self):
        numbers = []
        self.assertEqual(mean_absolute_deviation(numbers), 0)

if __name__ == '__main__':
    unittest.main()