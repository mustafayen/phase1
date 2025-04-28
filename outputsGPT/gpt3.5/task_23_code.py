# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



def lcm(a, b):
    # Find the greater number between a and b
    if a > b:
        greater = a
    else:
        greater = b
        
    while True:
        if greater % a == 0 and greater % b == 0:
            lcm = greater
            break
        greater += 1
        
    return lcm

# Test the function
print(lcm(4, 6))  # Output should be 12