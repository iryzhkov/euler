max_digits = int(input())

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

max_palindrome = 0
for i in range(10 ** max_digits - 1, 10 ** (max_digits - 1), -1):
    for j in range(10 ** max_digits - 1, i - 1, -1):
        n = i * j
        if is_palindrome(n):
            max_palindrome = max(max_palindrome, n)
print(max_palindrome)