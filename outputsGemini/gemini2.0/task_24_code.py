def missing_number(nums):
    """
    Finds the missing number in a list of distinct non-negative integers.
    The numbers are in the range [0, n] where n is the length of the list.

    Args:
        nums: A list of distinct non-negative integers.

    Returns:
        The missing number.
    """
    n = len(nums)
    expected_sum = n * (n + 1) // 2  # Sum of numbers from 0 to n
    actual_sum = sum(nums)
    return expected_sum - actual_sum
