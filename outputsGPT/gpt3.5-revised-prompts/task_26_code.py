# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



def most_frequent_element(lst):
    if not lst:
        return None
    
    freq_dict = {}
    for elem in lst:
        if elem in freq_dict:
            freq_dict[elem] += 1
        else:
            freq_dict[elem] = 1
    
    max_freq = max(freq_dict.values())
    most_frequent_elem = None
    for key, value in freq_dict.items():
        if value == max_freq:
            most_frequent_elem = key
            break
    
    return most_frequent_elem

# Test cases
print(most_frequent_element([1, 2, 2, 3, 3, 3]))  # Output: 3
print(most_frequent_element([1, 2, 2, 3, 3, 3, 2]))  # Output: 2
print(most_frequent_element([]))  # Output: None
