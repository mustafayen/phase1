# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


```python
def largest_divisor(n):
    max_divisor = 1
    for i in range(2, n//2 + 1):
        if n % i == 0:
            max_divisor = i
    return max_divisor
```

This function takes an integer `n` as input and returns the largest divisor of `n` that is less than `n`. It iterates through all numbers from 2 to `n//2` and checks if `n` is divisible by that number. If it is, it updates the `max_divisor` variable to that number. Finally, it returns the largest divisor found.