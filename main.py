def czy_palindrom(s):
    """
    Funkcja sprawdza, czy podany wyraz jest palindromem.

    Argumenty:
    s (str): Ciąg znaków do sprawdzenia

    Zwraca:
    bool: True, jeśli wyraz jest palindromem, False w przeciwnym wypadku.
    """
    s = s.lower()
    return s == s[::-1]


print(czy_palindrom("kajak"))
print(czy_palindrom("potop"))
print(czy_palindrom("pottop"))
print(czy_palindrom("Python"))
