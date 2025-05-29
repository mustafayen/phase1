# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022


import unittest
from task_4_code import fibonacci

class TestFibonacci(unittest.TestCase):

    def test_first_value(self):
        self.assertEqual(fibonacci(1), 0)

    def test_second_value(self):
        self.assertEqual(fibonacci(2), 1)

    def test_typical_case(self):
        self.assertEqual(fibonacci(6), 5)  # 0, 1, 1, 2, 3, 5

    def test_large_input(self):
        self.assertEqual(fibonacci(10), 34)

    def test_negative_input(self):
        self.assertEqual(
            fibonacci(-3),
            "Invalid input. Please enter a positive integer."
        )

if __name__ == '__main__':
    unittest.main()
