def is_prime(number):
    """
    Checks if a number is a prime number.

    Args:
        number: The number to check (integer).

    Returns:
        True if the number is prime, False otherwise.
        Returns False if the number is less than or equal to 1.
    """
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True
