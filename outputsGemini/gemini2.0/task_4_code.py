def fibonacci(n):
    """
    Calculates the nth Fibonacci number.

    Args:
        n: The index of the Fibonacci number to calculate (non-negative integer).

    Returns:
        The nth Fibonacci number.
        Returns 0 if n is 0.
        Returns 1 if n is 1.
    """
    if n < 0:
        raise ValueError("Input n must be a non-negative integer")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
