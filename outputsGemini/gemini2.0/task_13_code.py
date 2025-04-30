def get_unique_elements(lst):
    """
    Returns a new list containing only the unique elements from the input list.
    The order of elements in the output list should be the same as the first
    occurrence of each element in the input list.

    Args:
        lst: The input list.

    Returns:
        A new list containing only the unique elements from the input list.
    """
    unique_list = []
    seen = set()
    for item in lst:
        if item not in seen:
            seen.add(item)
            unique_list.append(item)
    return unique_list
