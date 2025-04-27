# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


def below_zero(operations):
    count = 0
    for num in operations:
        if num < 0:
            count += 1
    return count

# Example usage
operations = [1, -2, 3, -4, 5]
print(below_zero(operations))  # Output: 2