''' Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке. '''

f = open('my_file.txt', 'r+')
str_list = ['Abracadabra\n', 'Max\n', 'Leo\n', 'Marelyn\n']
f.writelines(str_list)

f = open('my_file.txt')
line_count = 0
for line in f:
    line_count += 1

    words = 0
    for i in line:
        if i != '':
            words += 1

    print(line, words)

print('Количество строк в файле: ', line_count)
f.close()
