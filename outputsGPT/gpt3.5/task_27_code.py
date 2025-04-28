# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



'''
Given a positive integer n, generate all valid combinations of n pairs of parentheses.

Example:
Input: 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
'''

def generate_parentheses(n):
    def backtrack(s, left, right):
        if len(s) == 2 * n:
            result.append(s)
            return
        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)
    
    result = []
    backtrack('', 0, 0)
    return result

# Test the function
n = 3
print(generate_parentheses(n))