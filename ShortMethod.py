# Common functions
def freq_map(arr):
    return {i: arr.count(i) for i in set(arr)}

def reverse_str(s):
    return s[::-1]

def is_palindrome(s):
    return s == s[::-1]

def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)
