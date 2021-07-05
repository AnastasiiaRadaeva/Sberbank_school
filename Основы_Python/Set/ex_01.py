import string
numbers = input()
set_num = set(numbers)
digits = frozenset(string.digits)
print(len(set_num.intersection(digits)))