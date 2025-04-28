# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



'''
This function performs a binary search on a sorted array to find the index of a target value.
If the target value is not found in the array, it returns -1.
'''

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1

# Example usage
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
print(binary_search(arr, target))  # Output: 3