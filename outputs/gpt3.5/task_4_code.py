# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


def mean_absolute_deviation(numbers):
    # Calculate the mean of the numbers
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute deviation of each number from the mean
    absolute_deviations = [abs(num - mean) for num in numbers]
    
    # Calculate the mean absolute deviation
    mean_absolute_deviation = sum(absolute_deviations) / len(numbers)
    
    return mean_absolute_deviation

# Example usage
numbers = [1, 2, 3, 4, 5]
print(mean_absolute_deviation(numbers)) # Output: 1.2