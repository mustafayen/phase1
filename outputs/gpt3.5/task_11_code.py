# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


def string_xor(a, b):
    result = ""
    for i in range(min(len(a), len(b))):
        if a[i] != b[i]:
            result += "1"
        else:
            result += "0"
    return result

# Example usage
a = "101010"
b = "110011"
print(string_xor(a, b))  # Output: "011001"