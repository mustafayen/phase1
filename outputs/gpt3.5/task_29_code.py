# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


def filter_by_prefix(strings, prefix):
    filtered_strings = [s for s in strings if s.startswith(prefix)]
    return filtered_strings

# Example usage
strings = ["apple", "banana", "orange", "grape"]
prefix = "b"
filtered_strings = filter_by_prefix(strings, prefix)
print(filtered_strings)  # Output: ["banana"]