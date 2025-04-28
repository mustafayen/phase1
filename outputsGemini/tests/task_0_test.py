import unittest
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False

class TestBelowZero(unittest.TestCase):
    def test_empty_list(self):
        self.assertFalse(below_zero([]))

    def test_never_below_zero(self):
        self.assertFalse(below_zero([1, 2, 3]))

    def test_goes_below_zero_once(self):
        self.assertTrue(below_zero([1, -2, 3]))

    def test_goes_below_zero_multiple_times(self):
        self.assertTrue(below_zero([-1, 2, -3, 4, -5]))

    def test_starts_below_zero(self):
        self.assertTrue(below_zero([-1, 1, 1]))

if __name__ == '__main__':
    unittest.main()
