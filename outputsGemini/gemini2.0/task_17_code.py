def find_pairs_with_sum(numbers, target):
    """
    Finds all unique pairs of numbers in a list that add up to a target sum.

    Args:
        numbers: A list of integers.
        target: The target sum (integer).

    Returns:
        A list of tuples, where each tuple represents a pair of numbers
        that add up to the target sum.
        Returns an empty list if no such pairs exist.
    """
    pairs = []
    seen = set()

    for i, num1 in enumerate(numbers):
        for j, num2 in enumerate(numbers):
            if i != j and num1 + num2 == target:
                # Ensure uniqueness of pairs (avoid duplicates like (1, 2) and (2, 1))
                pair = tuple(sorted((num1, num2)))
                if pair not in seen:
                    seen.add(pair)
                    pairs.append(pair)
    return pairs
