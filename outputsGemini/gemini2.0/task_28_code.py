def zigzag_conversion(s, num_rows):
    """
    Converts a string into a zigzag pattern with a given number of rows.

    Args:
        s: The input string.
        num_rows: The number of rows in the zigzag pattern.

    Returns:
        The string formed by reading the characters in the zigzag pattern.
    """
    if num_rows <= 1:
        return s

    rows = ["" for _ in range(num_rows)]
    row_index = 0
    direction = -1  # Start going down

    for char in s:
        rows[row_index] += char
        if row_index == 0 or row_index == num_rows - 1:
            direction *= -1  # Change direction at top and bottom rows
        row_index += direction

    return "".join(rows)
