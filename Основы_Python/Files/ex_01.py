import string
def email_gen(list_of_names):
    emails = []
    for i in list_of_names:
        letter = 1
        while i[1] + '.' + i[0][0:letter] + '@company.io' in emails:
            letter+=1
        emails.append(i[1] + '.' + i[0][0:letter] + '@company.io')
    return emails

def line_parser(line):
    list = line.split(",")
    i = 0
    while i < len(list):
        list[i] = list[i].strip()
        i += 1
    i = 0
    while i < len(list):
        if list[i] == '' and i != 0:
            email = [0, line]
            return(email)
        i += 1
    if list[3].isdigit() == False or len(list[3]) != 7 or list[0] != '':
        email = [0, line]
        return email
    name_surname = [list[1], list[2]]
    list_of_names.append(name_surname)
    email = [1, line]
    return(email)


list_of_names = []
new_info = []
file = open('/home/venus/Desktop/Nastya/Sberbank_school/Основы_Python/Files/task_file.txt')
for line in file:
    str = line_parser(line)
    new_info.append(str)
file.close()
emails = email_gen(list_of_names)
i = 0
j = 0
file = open('/home/venus/Desktop/Nastya/Sberbank_school/Основы_Python/Files/task_file_1.txt', 'w')
while i < len(new_info):
    if new_info[i][0] == 1:
        new_info[i][1] = emails[j] + new_info[i][1]
        j += 1
    file.write(new_info[i][1])
    i += 1
file.close()

