# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



# Function to count the number of vowels in a given string
def count_vowels(string):
    # Define a list of vowels
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    # Initialize a counter to keep track of the number of vowels
    count = 0
    
    # Iterate through each character in the string
    for char in string:
        # Check if the character is a vowel
        if char.lower() in vowels:
            count += 1
    
    return count

# Test the function with a sample string
string = "Hello World"
print(count_vowels(string)) # Output: 3