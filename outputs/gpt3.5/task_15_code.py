# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


def string_sequence(n):
    result = ""
    for i in range(1, n+1):
        result += str(i)
    return result

# Example usage
print(string_sequence(5))  # Output: "12345"