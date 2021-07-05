list = [1, 2, 5, 4, 4, 2, 7, 9]
list_2 = list.copy()
list_min = min(list_2)
list_max = max(list_2)
ind_min = list_2.index(list_min)
ind_max = list_2.index(list_max)
list_2[ind_min] = list_max
list_2[ind_max] = list_min
print(list_2)