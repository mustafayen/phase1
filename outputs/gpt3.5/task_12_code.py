# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


def longest(strings):
    max_length = 0
    longest_string = ""
    
    for string in strings:
        if len(string) > max_length:
            max_length = len(string)
            longest_string = string
    
    return longest_string

# Example usage
strings = ["apple", "banana", "orange", "kiwi"]
print(longest(strings))  # Output: "banana"