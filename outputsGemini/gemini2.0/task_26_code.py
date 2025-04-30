def most_frequent_element(lst):
    """
    Finds the most frequent element in a list.  If there is a tie, returns
    the element that appears first in the list.

    Args:
        lst: A list of elements.

    Returns:
        The most frequent element in the list.
        Returns None if the list is empty.
    """
    if not lst:
        return None

    counts = {}
    max_count = 0
    most_frequent = None

    for element in lst:
        counts[element] = counts.get(element, 0) + 1
        if counts[element] > max_count:
            max_count = counts[element]
            most_frequent = element

    return most_frequent
