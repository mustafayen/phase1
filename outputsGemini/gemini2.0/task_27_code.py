def generate_parentheses(n):
    """
    Generates all possible well-formed combinations of parentheses.

    Args:
        n: The number of pairs of parentheses.

    Returns:
        A list of strings, where each string is a valid combination of parentheses.
    """
    if n <= 0:
        return [""] if n == 0 else []  # Handle edge cases

    result = []

    def backtrack(open_count, close_count, current_combination):
        if open_count == n and close_count == n:
            result.append(current_combination)
            return

        if open_count < n:
            backtrack(open_count + 1, close_count, current_combination + "(")
        if close_count < open_count:
            backtrack(open_count, close_count + 1, current_combination + ")")

    backtrack(0, 0, "")
    return result
