list = [1, 2, 5, 4, 4, 2, 7, 1, 9]
i = 0
list_2 = []
while i < len(list):
    if i == 0 or list[i] > list[i - 1]:
        list_2.append(list[i])
    i += 1
print(list_2)