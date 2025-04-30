def anagram_check(str1, str2):
    """
    Checks if two strings are anagrams of each other.
    The function ignores spaces and is case-insensitive.

    Args:
        str1: The first string.
        str2: The second string.

    Returns:
        True if the strings are anagrams, False otherwise.
    """
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the lengths are equal
    if len(str1) != len(str2):
        return False

    # Count character frequencies
    char_counts = {}
    for char in str1:
        char_counts[char] = char_counts.get(char, 0) + 1
    for char in str2:
        char_counts[char] = char_counts.get(char, 0) - 1
        if char_counts[char] < 0:
            return False

    # If all counts are zero, the strings are anagrams
    return all(count == 0 for count in char_counts.values())
