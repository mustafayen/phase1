import unittest
from task_5_code import is_prime

class TestIsPrime(unittest.TestCase):

    def test_is_prime_with_2(self):
        self.assertTrue(is_prime(2))

    def test_is_prime_with_4(self):
        self.assertFalse(is_prime(4))

    def test_is_prime_with_a_prime_number(self):
        self.assertTrue(is_prime(7))

    def test_is_prime_with_a_non_prime_number(self):
        self.assertFalse(is_prime(9))
