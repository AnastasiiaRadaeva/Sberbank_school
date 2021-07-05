import re
import random

def email_gen(list_of_names):
    emails = []
    for i in list_of_names:
        letter = 1
        while i[1] + '.' + i[0][0:letter] + '@company.io' in emails:
            letter+=1
        emails.append(i[1] + '.' + i[0][0:letter] + '@company.io')
    return emails


def line_parser(line):
    if not (re.findall(r'\d\d\d\d\d\d\d', line) and re.findall(r',\s\w+,\s\w+,\s\w+,\s\w+', line)):
        not_valid_data.append(line)
        return
    list = line.split(",")
    i = 0
    while i < len(list):
        list[i] = list[i].strip()
        i += 1
    name_surname = [list[1], list[2]]
    list_of_names.append(name_surname)
    return line


def password_gen():
    len_of_password = random.randint(12, 20)
    count_of_digit = random.randint(1, len_of_password - 3)
    count_of_lower = random.randint(1, len_of_password - count_of_digit - 2)
    count_of_upper = random.randint(1, len_of_password - count_of_digit - count_of_lower - 1)
    count_of_spec = len_of_password - count_of_digit - count_of_lower - count_of_upper
    password = []
    while count_of_digit >= 0:
        password.append(random.choice('1234567890'))
        count_of_digit -= 1
    while count_of_lower >= 0:
        password.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
        count_of_lower -= 1
    while count_of_upper >= 0:
        password.append(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        count_of_upper -= 1
    while count_of_spec >= 0:
        password.append(random.choice('!@#$%^&*()-+'))
        count_of_spec -= 1
    random.shuffle(password)
    str_password = ''.join(password)
    return str_password


def fill_task_file():
    i = 1
    j = 0
    file = open('/home/venus/Desktop/Nastya/Sberbank_school/Основы_Python/Final_project/task_file_1.csv', 'w')
    file.write('PASSWORD, ' + new_info[0])
    while i < len(new_info):
        password = password_gen()
        new_info[i] = password + ', ' + emails[j] + new_info[i]
        file.write(new_info[i])
        i += 1
        j += 1
    file.close()


def fill_error_file():
    i = 0
    file_error_data = open('/home/venus/Desktop/Nastya/Sberbank_school/Основы_Python/Final_project/error_data.txt', 'w')
    while i < len(not_valid_data):
        file_error_data.write(not_valid_data[i])
        i += 1
    file_error_data.close()


list_of_names = []
new_info = []
not_valid_data = []
file = open('/home/venus/Desktop/Nastya/Sberbank_school/Основы_Python/Files/task_file.txt')
i = 0
for line in file:
    str = line
    if i != 0:
        str = line_parser(line)
    if str != None:
        new_info.append(str)
    i += 1
file.close()
emails = email_gen(list_of_names)
fill_task_file()
fill_error_file()
