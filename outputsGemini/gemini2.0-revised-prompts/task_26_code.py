

def most_frequent_element(lst):
    """
    Returns the element with the highest frequency in the list.
    If there is a tie in frequency, it returns the one that appears first in the list.
    """
    if not lst:
        return None

    frequency_map = {}
    for element in lst:
        frequency_map[element] = frequency_map.get(element, 0) + 1

    max_frequency = -1
    most_frequent = None

    # Iterate through the original list to find the element with the highest frequency
    # and handle ties by selecting the first encountered element.
    for element in lst:  # This loop is crucial for tie-breaking
        if frequency_map[element] > max_frequency:  # Only update if strictly greater
            max_frequency = frequency_map[element]
            most_frequent = element

    return most_frequent