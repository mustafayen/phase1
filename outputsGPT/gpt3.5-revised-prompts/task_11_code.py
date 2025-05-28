# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



'''
This function takes a nested list as input and returns a flattened list containing all the elements from the nested list.
'''

def flatten_list(nested_list):
    flattened_list = []
    
    for element in nested_list:
        if isinstance(element, list):
            flattened_list.extend(flatten_list(element))
        else:
            flattened_list.append(element)
    
    return flattened_list

# Example usage
nested_list = [1, [2, 3], [4, [5, 6]], 7]
flattened_list = flatten_list(nested_list)
print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6, 7]