def binary_search(arr, target):
    """
    Performs a binary search on a sorted array.

    Args:
        arr: A sorted list of integers.
        target: The integer to search for.

    Returns:
        The index of the target element in the array if found, otherwise -1.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # Integer division to find the middle index
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Target not found
