def sum_even_numbers(numbers):
    """
    Calculates the sum of all even numbers in a list.

    Args:
        numbers: A list of integers.

    Returns:
        The sum of the even numbers in the list.
        Returns 0 if the input list is empty or contains no even numbers.
    """
    even_sum = 0
    for number in numbers:
        if number % 2 == 0:
            even_sum += number
    return even_sum
