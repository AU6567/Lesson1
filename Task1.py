'''Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод __init__()), который должен принимать данные (список списков)
для формирования матрицы.
Подсказка: матрица — система некоторых математических величин,
расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31   22
37   43
51   86

3    5    32
2    4    6
-1   64   -8

3    5    8     3
8    3    7     1

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы
в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом
первой строки второй матрицы и т.д.
'''
class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        string = ''
        for i in self.my_list:
            for j in i:
                string = string + '%s\t' % (j)
            string = string[:-1]
            string = string + '\n'
        string = string[:-1]
        return string

    def __add__(self, other):
        result = []
        numbers = []
        for i in range(len(self.my_list)):
            for j in range(len(self.my_list[0])):
                new_list = other.my_list[i][j] + self.my_list[i][j]
                numbers.append(new_list)
                if len(numbers) == len(self.my_list[0]):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)


a = [[31, 22], [37, 43], [51, 86]]
b = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
c = [[3, 5, 8, 3], [8, 3, 7, 1]]
m_1 = Matrix(a)
m_2 = Matrix(b)
m_3 = Matrix(c)

print('\nМатрица 1')
print(m_1, '\n')

print('Матрица 2')
print(m_2, '\n')

print('Матрица 3')
print(m_3, '\n')

print('Сумма матриц 1, 2 и 3')
print(m_1 + m_2)
