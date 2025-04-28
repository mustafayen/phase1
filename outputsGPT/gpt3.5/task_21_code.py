# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



The function `move_zeros` takes a list of numbers as input and moves all the zeros to the end of the list while maintaining the order of the non-zero elements.

Here is the implementation of the `move_zeros` function:

```python
def move_zeros(nums):
    zero_count = nums.count(0)
    nums = [num for num in nums if num != 0]
    nums.extend([0] * zero_count)
    return nums

# Test the function
nums = [0, 1, 0, 3, 12]
print(move_zeros(nums))  # Output: [1, 3, 12, 0, 0]
```

In this implementation, we first count the number of zeros in the input list. Then, we create a new list `nums` by filtering out all the zeros from the input list. Finally, we extend the new list with the required number of zeros at the end.