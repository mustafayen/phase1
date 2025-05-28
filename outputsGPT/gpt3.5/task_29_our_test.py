# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022


import unittest
from task_29_code import is_valid_sudoku

class TestTask29(unittest.TestCase):

    def test_case_1(self):
        board = [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]
        self.assertTrue(is_valid_sudoku(board))

    def test_case_2(self):
        board = [
            ["8","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]
        self.assertFalse(is_valid_sudoku(board))  # duplicate 8 in top left box

    def test_case_3(self):
        board = [["."]*9 for _ in range(9)]
        self.assertTrue(is_valid_sudoku(board))

    def test_case_4(self):
        board = [["1"]*9 for _ in range(9)]
        self.assertFalse(is_valid_sudoku(board))  # all same

    def test_case_5(self):
        board = [["."]*9 for _ in range(9)]
        board[0][0] = "5"
        board[0][1] = "5"
        self.assertFalse(is_valid_sudoku(board))  # same row

if __name__ == '__main__':
    unittest.main()
