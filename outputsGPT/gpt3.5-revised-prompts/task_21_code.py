# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



def move_zeros(nums):
    zero_count = 0
    
    for i in range(len(nums)):
        if nums[i] == 0:
            zero_count += 1
        else:
            nums[i - zero_count] = nums[i]
    
    for i in range(len(nums) - zero_count, len(nums)):
        nums[i] = 0

# Example
nums = [0, 1, 0, 3, 12]
move_zeros(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]
