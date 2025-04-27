# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


import unittest

def rescale_to_unit(numbers):
    max_num = max(numbers)
    min_num = min(numbers)
    rescaled_numbers = [(num - min_num) / (max_num - min_num) for num in numbers]
    return rescaled_numbers

class TestRescaleToUnit(unittest.TestCase):

    def test_rescale_to_unit_positive_numbers(self):
        numbers = [1, 2, 3, 4, 5]
        expected_result = [0.0, 0.25, 0.5, 0.75, 1.0]
        self.assertEqual(rescale_to_unit(numbers), expected_result)

    def test_rescale_to_unit_negative_numbers(self):
        numbers = [-5, -4, -3, -2, -1]
        expected_result = [0.0, 0.25, 0.5, 0.75, 1.0]
        self.assertEqual(rescale_to_unit(numbers), expected_result)

    def test_rescale_to_unit_mixed_numbers(self):
        numbers = [-2, 0, 2, 4, 6]
        expected_result = [0.0, 0.25, 0.5, 0.75, 1.0]
        self.assertEqual(rescale_to_unit(numbers), expected_result)

    def test_rescale_to_unit_duplicate_numbers(self):
        numbers = [1, 1, 1, 1, 1]
        expected_result = [0.0, 0.0, 0.0, 0.0, 0.0]
        self.assertEqual(rescale_to_unit(numbers), expected_result)

if __name__ == '__main__':
    unittest.main()