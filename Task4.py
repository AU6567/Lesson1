'''Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''
with open('number.txt', 'r') as f:
    my_list = list()
    for line in f.readlines():
        my_list.extend(line.split(' '))
print(my_list)

new_list = ['Один — 1', 'Два — 2', 'Три — 3', 'Четыре — 4']

x = 0
for i in range(0, len(my_list), 3):
    my_list[i] = new_list[x]
    x += 1

print(my_list)
obj_f = open('number.txt', 'w', encoding='utf-8')
obj_f.writelines(my_list)
obj_f.close()
