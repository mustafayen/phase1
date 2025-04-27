# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


```python
def how_many_times(string, substring):
    count = 0
    start = 0
    while True:
        start = string.find(substring, start) # Find the next occurrence of the substring
        if start == -1: # If no more occurrences are found, break out of the loop
            break
        count += 1
        start += 1 # Move to the next character in the string
    return count
```

This function takes in two parameters, `string` and `substring`, and returns the number of times the `substring` appears in the `string`. It uses the `find` method to search for the `substring` in the `string` and increments the count each time it finds a match.