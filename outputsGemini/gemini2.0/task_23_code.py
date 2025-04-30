def lcm(a, b):
    """
    Calculates the least common multiple (LCM) of two integers.

    Args:
        a: The first integer.
        b: The second integer.

    Returns:
        The least common multiple of a and b.
        Returns 0 if either a or b is 0.
    """
    if a == 0 or b == 0:
        return 0  # LCM is 0 if either number is 0

    # Calculate GCD using the Euclidean algorithm
    a_copy, b_copy = a, b  # Preserve original values for multiplication
    while b_copy:
        a_copy, b_copy = b_copy, a_copy % b_copy
    gcd_val = a_copy

    return (a * b) // gcd_val
