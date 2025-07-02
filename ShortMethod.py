# Common functions
def freq_map(arr):
    return {i: arr.count(i) for i in set(arr)}

def reverse_str(s):
    return s[::-1]

def is_palindrome(s):
    return s == s[::-1]

def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)
#BASIC DSA HELPER 
# ✅ Count frequencies
from collections import Counter
def freq_map(arr):
    return dict(Counter(arr))

# ✅ Reverse string
def reverse_str(s):
    return s[::-1]

# ✅ Is palindrome
def is_palindrome(s):
    return s == s[::-1]

# ✅ Factorial (iterative)
def factorial(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

# ✅ Prime check
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
33ARRAY LISTS 
# ✅ Remove duplicates
def remove_dupes(arr):
    return list(set(arr))

# ✅ Find max 2 numbers
def top_two(arr):
    first = second = float('-inf')
    for n in arr:
        if n > first:
            first, second = n, first
        elif n > second:
            second = n
    return first, second

# ✅ Prefix sum array
def prefix_sum(arr):
    for i in range(1, len(arr)):
        arr[i] += arr[i-1]
    return arr
 #STRINGS 

# ✅ Count vowels
def count_vowels(s):
    return sum(1 for ch in s.lower() if ch in 'aeiou')

# ✅ Most frequent char
def most_freq_char(s):
    return Counter(s).most_common(1)[0]

# ✅ Anagram check
def is_anagram(a, b):
    return Counter(a) == Counter(b)
#SORT AND SEARCH 
# ✅ Custom sort by length
def sort_by_len(arr):
    return sorted(arr, key=len)

# ✅ Binary search
def binary_search(arr, target):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
#HMAP DICT # ✅ Frequency dict of chars
def char_freq_map(s):
    return dict(Counter(s))

# ✅ First non-repeating char
def first_unique_char(s):
    freq = Counter(s)
    for ch in s:
        if freq[ch] == 1:
            return ch
    return None

#MATH 

# ✅ GCD / HCF
from math import gcd

# ✅ LCM
def lcm(x, y):
    return abs(x*y) // gcd(x, y)

# ✅ Fibonacci (iterative)
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a
