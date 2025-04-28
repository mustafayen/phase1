# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



# Function to check if two strings are anagrams
def anagram_check(str1, str2):
    # Remove spaces and convert both strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if the length of both strings are equal
    if len(str1) != len(str2):
        return False
    
    # Sort the characters in both strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    
    # Check if the sorted strings are equal
    if sorted_str1 == sorted_str2:
        return True
    else:
        return False

# Test the function
print(anagram_check("listen", "silent")) # True
print(anagram_check("hello", "world")) # False