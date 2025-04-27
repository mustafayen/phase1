# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


def sum_product(numbers):
    sum_of_numbers = sum(numbers)
    product_of_numbers = 1
    for num in numbers:
        product_of_numbers *= num
    return sum_of_numbers, product_of_numbers