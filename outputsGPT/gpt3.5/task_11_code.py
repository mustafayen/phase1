# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



```python
def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list

# Example usage
nested_list = [1, [2, 3], [4, [5, 6]], 7]
print(flatten_list(nested_list))  # Output: [1, 2, 3, 4, 5, 6, 7]
```