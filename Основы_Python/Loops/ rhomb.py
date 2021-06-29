a = int(input("Введите число: "))
if a > 9:
    print ("Error")
else:
    for i in range (1, a + 1):
        c = a - i
        while c > 0 :
            print(" ", end="")
            c -= 1
        for j in range (1, i + 1): 
            print (j, end="")
        j -= 1
        while j >= 1:
            print (j, end="")
            j -= 1
        print("")
    a_2 = a
    a -= 1
    while a > 0:
        c = a_2 - a
        while c > 0 :
            print(" ", end="")
            c -= 1
        for j in range (1, a + 1): 
            print (j, end="")
        j -= 1
        while j >= 1:
            print (j, end="")
            j -= 1
        print("")
        a -= 1


