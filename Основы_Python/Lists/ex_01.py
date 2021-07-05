list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
i = 0
list_2 = []
while i < len(list):
    if i % 2 == 0:
        list_2.append(list[i])
    i += 1
print(list_2)
