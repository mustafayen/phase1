# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



'''
Given a list of numbers from 0 to n with one number missing, find and return the missing number.

Example:
Input: [3, 0, 1]
Output: 2
'''

def missing_number(nums):
    n = len(nums)
    total_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    
    return total_sum - actual_sum

# Test the function
print(missing_number([3, 0, 1])) # Output: 2