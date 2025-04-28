# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



# Function to check if a word is a palindrome
def is_palindrome(word):
    # Convert word to lowercase to make case-insensitive comparison
    word = word.lower()
    
    # Remove any spaces from the word
    word = word.replace(" ", "")
    
    # Check if the word is equal to its reverse
    if word == word[::-1]:
        return True
    else:
        return False

# Test the function
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False
print(is_palindrome("A man a plan a canal Panama"))  # True