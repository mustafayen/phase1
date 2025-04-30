def calculate_median(numbers):
    """
    Calculates the median of a list of numbers.

    Args:
        numbers: A list of numbers.

    Returns:
        The median of the numbers in the list.
        Returns None if the list is empty.
    """
    if not numbers:
        return None

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        # Even number of elements, average the middle two
        mid1 = sorted_numbers[n // 2 - 1]  # Index of the first middle element
        mid2 = sorted_numbers[n // 2]      # Index of the second middle element
        median = (mid1 + mid2) / 2
    else:
        # Odd number of elements, take the middle one
        median = sorted_numbers[n // 2]  # Index of the middle element
    return median
