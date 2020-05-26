'''Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''

f = open('student_subject.txt', encoding='utf-8')
my_list = f.read().split('\n')[:-1]
print(my_list)

my_dict = {}
#
# for item in my_list:
#     key = item.split(' ')[0]
#     value = item.split(' ')[1:]
#     my_dict[key] = value
# print(dict)
#
# print('\n Общее количество занятий по предметам')
# for i in my_dict:
#     list = my_dict[i]
#     sum_n = 0
#     for j in range(0, len(list)):
#         sum_n += int(list[j])
#     print(i, ':', sum_n)

for i in my_list:
    if '\n' in i:
        my_list[my_list.index(i)] = my_list[my_list.index(i)].replace('\n', '')

for i in my_list:
    if '--' in i:
        my_list.pop(my_list.index('--'))
        my_list.pop(my_list.index('--'))

a = 0
for i in my_list:
    if i.isdigit():
        a += int(i)

new_list = my_list[0:1]
new_list.append(a)

my_dict[new_list[0]] = new_list[1]

print(my_dict)


f.close()
