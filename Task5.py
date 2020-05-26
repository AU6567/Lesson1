''' Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''

with open('list_num.txt', 'w') as f:
    my_list = [i for i in range(1, 50)]
    print(f'In my file {len(my_list)} numbers')
    for i in my_list:
        f.write(str(i)+' ')

with open('list_num.txt', 'r') as f:
    my_str = f.read()
    my_list = my_str.split(' ')
    result = 0
    for i in my_list:
        if not i.isdigit():
            my_list.pop(my_list.index(i))
    for i in my_list:
        result += int(i)
    print(f'Sum of all numbers are {result}.')

# print('Файл. Закрыт: ', f.closed)
# print('Файл. Режим: ', f.mode)
