# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


def rolling_max(numbers):
    max_values = []
    for i in range(len(numbers)):
        if i == 0:
            max_values.append(numbers[i])
        else:
            max_values.append(max(numbers[:i+1]))
    return max_values