def is_valid_sudoku(board):
    """
    Checks if a given Sudoku board is valid.  This function only checks
    the validity of the *filled* cells.  It does not check if the Sudoku
    is solvable.

    Args:
        board: A 9x9 list of lists representing the Sudoku board.
               Empty cells are represented by the character '.'.

    Returns:
        True if the board is valid, False otherwise.
    """
    def is_valid_unit(unit):
        """
        Checks if a 1D list (row, column, or subgrid) is valid.
        """
        seen = set()
        for cell in unit:
            if cell != '.':
                if cell in seen or not '1' <= cell <= '9':
                    return False
                seen.add(cell)
        return True

    # Check rows
    for row in board:
        if not is_valid_unit(row):
            return False

    # Check columns
    for col in zip(*board):  # Transpose for columns
        if not is_valid_unit(col):
            return False

    # Check subgrids
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not is_valid_unit(subgrid):
                return False

    return True
