# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
arg_1 = int(input('Введите число - первый позиционный аргумент: '))
arg_2 = int(input('Введите число - второй позиционный аргумент: '))
def my_sum(arg_1, arg_2):
    try:
        arg_1 / arg_2 or arg_2 / arg_1
    except ZeroDivisionError:
        print('Деление на 0')
        return 0
    else:
        return arg_1 / arg_2 or arg_2 / arg_1

arguments = my_sum(arg_1, arg_2)
print('Получилось: ', round(arguments, 2))
