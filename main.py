def is_palindrome(s):

    s = s.lower()
    return s == s[::-1]


print(is_palindrome("kajak"))
print(is_palindrome("potop"))
print(is_palindrome("pottop"))
print(is_palindrome("Python"))
