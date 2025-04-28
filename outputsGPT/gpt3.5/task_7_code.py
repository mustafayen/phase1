# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



'''
This function takes a string as input and returns the count of vowels in the string.
Vowels are 'a', 'e', 'i', 'o', 'u'.
'''

def count_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    
    for char in string:
        if char.lower() in vowels:
            count += 1
    
    return count

# Example usage
print(count_vowels("hello")) # Output: 2
print(count_vowels("Python")) # Output: 1
print(count_vowels("programming")) # Output: 3