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
    pairs = set()  # Use a set of tuples to automatically handle uniqueness
    seen = set()  # To track numbers encountered so far

    for num in numbers:
        complement = target - num
        # If the complement has been seen and we haven't already added this specific pair
        # (to handle cases like (2,2) for target=4, ensure num is not already in the pairs set with itself if it's the only one)
        if complement in seen:
            # Ensure the pair is sorted to handle (a,b) and (b,a) as the same pair
            pair = tuple(sorted((num, complement)))
            pairs.add(pair)
        seen.add(num)

    # Convert the set of pairs to a list and sort it for consistent testing
    # The order of pairs in the output list might not be deterministic otherwise.
    return sorted(list(pairs))