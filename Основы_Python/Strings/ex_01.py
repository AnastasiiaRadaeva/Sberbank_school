s = "Abraсadabra"
print("1:", s[2])
print("2:", s[len(s) - 2])
print("3:", s[0:5])
print("4:", s[0:len(s)-2])
print("5:", end=" ")
c = 0
len_s = len(s)
while c < len_s:
    if c % 2 == 0:
        print (s[c], end="")
    c += 1
print("\n6:", end=" ")
c = 0
len_s = len(s)
while c < len_s:
    if c % 2 == 1:
        print (s[c], end="")
    c += 1
print("\n7:", s[::-1])
print("8:", s[::-2])
print("9:", len(s))







