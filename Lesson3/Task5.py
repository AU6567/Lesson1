# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и
# после этого завершить программу.
# def sum(line_number):
#     line_number = line_number.split()
#     line_number2 = []
#     for i in line_number:
#         line_number2.append((int(i)))
#     return sum(line_number2)
#
# x = 0
# while 1:
#     line_number = input("Введите строку чисел, разделенных пробелом: ")
#     if line_number.endswith('*'):
#         line_number = line_number[:-1]
#         x += sum(line_number)
#         print("Сумма чисел: ", x)
#         break
#     x += sum(line_number)
#     print("Сумма чисел: ", x)

def sum_of_number_in_list(list):
    b = 0
    for i in list:
        if i == '*':
            break
        else:
            try:
                a = int(i)
                b += a
            except ValueError:
                print('Не вводите больше одного пробела между буквами, или не ставьте пробел в конце!\n'
                      'Или при выходе перед * не ставьте пробел')

    return b

growing_number = 0

while True:
    ask_numbers_row = input('Введите строку чисел, разделенных пробелом! Или нажмите * для выхода: ')

    if '*' in ask_numbers_row:
        my_list = ask_numbers_row.split(' ')
        result = sum_of_number_in_list(my_list)
        growing_number += result
        print(growing_number)
        break

    else:
        my_list = ask_numbers_row.split(' ')
        result = sum_of_number_in_list(my_list)
        growing_number += result
        print(growing_number)
