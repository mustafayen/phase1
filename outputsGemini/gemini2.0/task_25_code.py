def check_brackets(string):
    """
    Checks if the brackets in a string are balanced.  This includes
    parentheses (), square brackets [], and curly braces {}.

    Args:
        string: The input string.

    Returns:
        True if the brackets are balanced, False otherwise.
    """
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}

    for char in string:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
    return not stack  # Stack should be empty if all brackets are balanced
