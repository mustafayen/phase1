# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



# Function to find the greatest common divisor (GCD) of two numbers a and b
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Test the function
print(gcd(12, 18))  # Output: 6
print(gcd(24, 36))  # Output: 12
print(gcd(17, 23))  # Output: 1