import string
s = input("Введите пароль: ")
if len(s) < 12:
    print("Wrong count of letters")
alphabet = frozenset(string.ascii_lowercase)
if not any(letter in alphabet for letter in s):
    print("Need lowercase")
alphabet_up = frozenset(string.ascii_uppercase)
if not any(letter in alphabet_up for letter in s):
    print("Need uppercase")
digit = frozenset(string.digits)
if not any(letter in digit for letter in s):
    print("Need digit")
spec_symb = "!@#$%^&*()-+"
if not any(letter in spec_symb for letter in s):
    print("Need special symbol")