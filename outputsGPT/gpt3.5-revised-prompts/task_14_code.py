# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



def find_median(nums):
    nums.sort()
    n = len(nums)
    
    if n % 2 == 0:
        mid1 = nums[n//2 - 1]
        mid2 = nums[n//2]
        return (mid1 + mid2) / 2
    else:
        return nums[n//2]

# Example
nums = [3, 1, 7, 5, 9, 2]
print(find_median(nums))  # Output: 4.0
