def remove_duplicates(lst):
    """
    Removes duplicate elements from a list, preserving the original order.

    Args:
        lst: The input list.

    Returns:
        A new list with duplicates removed.
    """
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
