def is_palindrome(word):
    """
    Checks if a given word is a palindrome.
    The function ignores case.

    Args:
        word: The input string.

    Returns:
        True if the word is a palindrome, False otherwise.
    """
    word = word.lower()
    return word == word[::-1]
