# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



# Function to find pairs in a list of numbers that add up to a given target sum
def find_pairs_with_sum(numbers, target):
    pairs = []
    seen = set()
    
    for num in numbers:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    
    return pairs

# Example usage
numbers = [1, 2, 3, 4, 5]
target = 6
print(find_pairs_with_sum(numbers, target)) # Output: [(1, 5), (2, 4)]