# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
# и возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().
def int_func(text):
    text = text[:]
    text = text[0].capitalize() + text[1:]
    return text

print(int_func('text'))
print(int_func('abrakadabra'))


def int_func(text):
    return ' '.join(word[:1].upper() + word[1:] for word in text.split(' '))

text = input('Введите слово из маленьких латинских букв: ')
print(int_func(text))