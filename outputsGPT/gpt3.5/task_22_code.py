# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



# Function to find the greatest common divisor (GCD) of two numbers using Euclidean algorithm
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Test the function
print(gcd(12, 8))  # Output: 4
print(gcd(17, 5))  # Output: 1