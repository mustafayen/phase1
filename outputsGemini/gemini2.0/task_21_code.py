def move_zeros(nums):
    """
    Moves all zeros in a list to the end of the list while maintaining the
    relative order of the non-zero elements. This should be done in-place.

    Args:
        nums: A list of integers.

    Returns:
        None. The list is modified in-place.
    """
    n = len(nums)
    # Initialize a pointer to track the position to insert the next non-zero element
    insert_pos = 0

    # Iterate through the list
    for i in range(n):
        if nums[i] != 0:
            # If the current element is not zero, move it to the insert position
            nums[insert_pos] = nums[i]
            insert_pos += 1

    # Fill the remaining positions with zeros
    for i in range(insert_pos, n):
        nums[i] = 0
