# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



# Function to get unique elements from a list
def get_unique_elements(lst):
    unique_elements = []
    
    # Iterate through the list
    for element in lst:
        # Check if the element is not already in the unique_elements list
        if element not in unique_elements:
            unique_elements.append(element)
    
    return unique_elements

# Test the function
lst = [1, 2, 3, 4, 2, 3, 5]
print(get_unique_elements(lst))  # Output: [1, 2, 3, 4, 5]