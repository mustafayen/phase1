def count_vowels(string):
    """
    Counts the number of vowels (a, e, i, o, u) in a given string.
    The function is case-insensitive.

    Args:
        string: The input string.

    Returns:
        The number of vowels in the string.
    """
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for char in string:
        if char in vowels:
            vowel_count += 1
    return vowel_count
