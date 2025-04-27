# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


def count_distinct_characters(string):
    distinct_chars = set(string)
    return len(distinct_chars)

# Example usage
string = "hello"
print(count_distinct_characters(string)) # Output: 4