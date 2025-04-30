def flatten_list(nested_list):
    """
    Flattens a nested list into a single-level list.

    Args:
        nested_list: A list that may contain nested lists.

    Returns:
        A new list containing all elements from the nested list, with no nesting.
    """
    flattened_list = []
    for item in nested_list:
        if isinstance(item, list):
            flattened_list.extend(flatten_list(item))  # Recursive call
        else:
            flattened_list.append(item)
    return flattened_list
