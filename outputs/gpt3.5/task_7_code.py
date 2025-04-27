# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


def filter_by_substring(strings, substring):
    filtered_strings = []
    for string in strings:
        if substring in string:
            filtered_strings.append(string)
    return filtered_strings

# Example usage
strings = ["apple", "banana", "orange", "grape"]
substring = "an"
filtered_strings = filter_by_substring(strings, substring)
print(filtered_strings)  # Output: ['banana', 'orange']