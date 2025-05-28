# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



def longest_word(words):
    if not words:
        return ""
    
    max_length = 0
    longest_word = ""
    
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
            longest_word = word
    
    return longest_word

# Example
words = ["apple", "banana", "orange", "kiwi"]
print(longest_word(words))  # Output: "banana"
