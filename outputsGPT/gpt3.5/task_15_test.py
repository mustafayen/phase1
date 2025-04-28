# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

class TestFactorial(unittest.TestCase):

    def test_factorial_of_0(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_of_1(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_of_positive_number(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_of_negative_number(self):
        self.assertRaises(ValueError, factorial, -1)

if __name__ == '__main__':
    unittest.main()