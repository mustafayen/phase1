# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

# Test the function
print(lcm(3, 5))  # Output: 15
print(lcm(0, 5))  # Output: 0
print(lcm(10, 15))  # Output: 30
