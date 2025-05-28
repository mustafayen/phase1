# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Test the function
try:
    n = int(input("Enter a non-negative integer: "))
    result = factorial(n)
    print(f"The factorial of {n} is {result}")
except ValueError as e:
    print(e)

