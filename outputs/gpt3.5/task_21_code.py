# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


def rescale_to_unit(numbers):
    min_num = min(numbers)
    max_num = max(numbers)
    rescaled_numbers = [(num - min_num) / (max_num - min_num) for num in numbers]
    return rescaled_numbers