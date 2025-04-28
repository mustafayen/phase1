# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest

def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

class TestFibonacci(unittest.TestCase):

    def test_fibonacci_0(self):
        self.assertEqual(fibonacci(0), "Invalid input")

    def test_fibonacci_1(self):
        self.assertEqual(fibonacci(1), 0)

    def test_fibonacci_2(self):
        self.assertEqual(fibonacci(2), 1)

    def test_fibonacci_5(self):
        self.assertEqual(fibonacci(5), 3)

    def test_fibonacci_10(self):
        self.assertEqual(fibonacci(10), 34)

if __name__ == '__main__':
    unittest.main()