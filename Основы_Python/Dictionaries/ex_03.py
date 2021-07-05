str = input()
list = str.split(" ")
dict_ = dict()
for i in list:
    if dict_.get(i, -1) == -1:
        dict_[i] = 1
    else:
        dict_[i] += 1
print(dict_.values())