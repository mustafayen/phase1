# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


def intersperse(numbers, delimiter):
    result = []
    for i in range(len(numbers)):
        result.append(numbers[i])
        if i != len(numbers) - 1:
            result.append(delimiter)
    return result

# Example usage
numbers = [1, 2, 3, 4, 5]
delimiter = ","
print(intersperse(numbers, delimiter))  # Output: [1, ',', 2, ',', 3, ',', 4, ',', 5]