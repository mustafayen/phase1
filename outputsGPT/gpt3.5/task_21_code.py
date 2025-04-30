# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022




def move_zeros(nums):
    zero_count = nums.count(0)
    nums = [num for num in nums if num != 0]
    nums.extend([0] * zero_count)
    return nums

# Test the function
nums = [0, 1, 0, 3, 12]
print(move_zeros(nums))  # Output: [1, 3, 12, 0, 0]

