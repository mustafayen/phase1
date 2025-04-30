def group_anagrams(words):
    """
    Groups a list of words into sublists, where each sublist contains words
    that are anagrams of each other.  The order of words in the output
    does not matter.

    Args:
        words: A list of strings.

    Returns:
        A list of lists, where each inner list contains words that are anagrams
        of each other.
    """
    anagram_groups = {}
    for word in words:
        # Sort the characters of the word to use as a key
        sorted_word = "".join(sorted(word.lower())) #convert word to lower case
        if sorted_word not in anagram_groups:
            anagram_groups[sorted_word] = []
        anagram_groups[sorted_word].append(word)
    return list(anagram_groups.values())
