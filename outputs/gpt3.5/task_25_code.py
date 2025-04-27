# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


Here is a complete Python function that factorizes a given number `n` and returns a list of its prime factors:

```python
def factorize(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# Test the function
n = 60
print(factorize(n))  # Output: [2, 2, 3, 5]
```

This function uses a while loop to iterate through all possible factors of the given number `n`. It checks if `n` is divisible by the current factor `i`, and if so, it divides `n` by `i` and appends `i` to the list of factors. This process continues until `n` is no longer divisible by `i`. Finally, if `n` is greater than 1, it appends `n` to the list of factors.