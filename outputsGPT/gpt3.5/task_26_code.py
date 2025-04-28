# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



def most_frequent_element(lst):
    count_dict = {}
    for element in lst:
        if element in count_dict:
            count_dict[element] += 1
        else:
            count_dict[element] = 1
    
    max_count = 0
    most_frequent_element = None
    for key, value in count_dict.items():
        if value > max_count:
            max_count = value
            most_frequent_element = key
    
    return most_frequent_element

# Example usage
lst = [1, 2, 3, 1, 2, 1, 3, 1, 4]
print(most_frequent_element(lst))  # Output: 1