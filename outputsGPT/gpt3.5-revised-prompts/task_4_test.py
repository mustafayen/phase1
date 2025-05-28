# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest
from task_4_code import fibonacci

class TestFibonacci(unittest.TestCase):

    def test_fibonacci_0(self):
        self.assertEqual(fibonacci(0), 0)

    def test_fibonacci_1(self):
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_2(self):
        self.assertEqual(fibonacci(2), 1)

    def test_fibonacci_5(self):
        self.assertEqual(fibonacci(5), 5)

    def test_fibonacci_10(self):
        self.assertEqual(fibonacci(10), 55)

if __name__ == '__main__':
    unittest.main()
