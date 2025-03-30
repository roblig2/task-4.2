def czy_palindrom(s):

    s = s.lower()
    return s == s[::-1]


print(czy_palindrom("kajak"))
print(czy_palindrom("potop"))
print(czy_palindrom("pottop"))
print(czy_palindrom("Python"))
