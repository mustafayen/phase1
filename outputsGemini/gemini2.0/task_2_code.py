def find_longest_word(words):
    """
    Finds the longest word in a list of words.

    Args:
        words: A list of strings.

    Returns:
        The longest word in the list.
        If the input list is empty, returns an empty string.
        If there are multiple words with the same longest length, returns the first one encountered.
    """
    if not words:
        return ""

    longest_word = words[0]
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word
