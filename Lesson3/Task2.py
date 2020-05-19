# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
# info = {
#     'Имя пользователя': ('Имя: ', str),
#     'Фамилия пользователя': ('Фамилия: ', str),
#     'Год рождения пользователя': ('Год рождения: ', int),
#     'Город проживания': ('Город: ', str),
#     'Email пользователя': ('Email: ', str),
#     'Телефон пользователя': ('Телефон: ', int)
# }
# user_list = []
# user = {}
# for key, value in info.items():
#     while True:
#         user_value = input(f'{value[0]}\n')
#         try:
#             user_value = value[1](user_value)
#         except ValueError as e:
#             print(f'{e}\n неверное значение данных')
#             continue
#         user[key] = user_value
#         break
#     user_list.append(user)
def users(name, surname, birth_year, residence_city, email, phone_number):
    print(f'Имя - {name}, Фамилия - {surname}, Год рождения - {birth_year}, '
          f'Город проживания - {residence_city}, email - {email}, Телефонный номер - {phone_number}')
    print(name, surname, birth_year, residence_city, email, phone_number)

print('Введите следующие данные')
name = input('Имя: ')
surname = input('Фамилия: ')
birth_year = int(input('Год рождения: '))
residence_city = input('Город проживания: ')
email = input('email: ')
phone_number = int(input('Телефонный номер: '))

users(name, surname, birth_year, residence_city, email, phone_number)
