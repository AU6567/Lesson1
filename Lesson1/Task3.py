# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

# n = int(input('Введите число n: '))
#
# num1 = int("%s" % n)
# num2 = int("%s%s" % (n, n))
# num3 = int("%s%s%s" % (n, n, n))
# print(num1 + num2 + num3)

# n = int(input('Введите число n: '))
# sum_n = str(n)
#
# num1 = sum_n + sum_n
# num2 = sum_n + sum_n + sum_n
#
# total = n + int(num1) + int(num2)
# print('Ваше число: ', total)

n = input('Введите число n: ')
nn = int(n+n)
nnn = int(n+n+n)
n = int(n)
result = n+nn+nnn
print(result)
