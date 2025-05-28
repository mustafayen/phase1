# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



# Function to check if a number is prime
def is_prime(number):
    # If number is less than 2, it is not prime
    if number < 2:
        return False
    # Check for factors from 2 to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Test the function
print(is_prime(5))  # Output: True
print(is_prime(10)) # Output: False