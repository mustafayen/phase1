# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


import unittest

def sum_product(numbers):
    sum_of_numbers = sum(numbers)
    product_of_numbers = 1
    for num in numbers:
        product_of_numbers *= num
    return sum_of_numbers, product_of_numbers

class TestSumProduct(unittest.TestCase):

    def test_sum_product_positive_numbers(self):
        result = sum_product([1, 2, 3, 4, 5])
        self.assertEqual(result, (15, 120))

    def test_sum_product_negative_numbers(self):
        result = sum_product([-1, -2, -3, -4, -5])
        self.assertEqual(result, (-15, -120))

    def test_sum_product_mixed_numbers(self):
        result = sum_product([1, -2, 3, -4, 5])
        self.assertEqual(result, (3, 120))

    def test_sum_product_empty_list(self):
        result = sum_product([])
        self.assertEqual(result, (0, 1))

if __name__ == '__main__':
    unittest.main()