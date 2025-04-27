# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


def flip_case(string):
    flipped_string = ""
    for char in string:
        if char.islower():
            flipped_string += char.upper()
        elif char.isupper():
            flipped_string += char.lower()
        else:
            flipped_string += char
    return flipped_string

# Example usage
print(flip_case("Hello World"))  # Output: hELLO wORLD