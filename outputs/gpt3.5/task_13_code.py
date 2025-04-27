# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


def greatest_common_divisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Example usage
print(greatest_common_divisor(24, 36))  # Output: 12