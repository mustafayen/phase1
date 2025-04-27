# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result

# Example usage
strings = ["hello", "world", "!"]
print(concatenate(strings))  # Output: helloworld!