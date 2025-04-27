# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


def make_palindrome(string):
    reversed_string = string[::-1]
    palindrome = string + reversed_string
    return palindrome

# Example usage
print(make_palindrome("hello"))  # Output: "helloolleh"