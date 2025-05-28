# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022




def find_pairs(numbers, target):
    pairs = set()
    seen = set()
    
    for num in numbers:
        complement = target - num
        if complement in seen:
            pair = (min(num, complement), max(num, complement))
            pairs.add(pair)
        seen.add(num)
    
    return list(pairs)

# Example usage
numbers = [2, 4, 3, 2, 1, 5, 6, 7, 8, 9]
target = 10
print(find_pairs(numbers, target))  # Output: [(1, 9), (2, 8), (3, 7), (4, 6)]

