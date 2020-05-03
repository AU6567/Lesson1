# 2. Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
import time

seconds = int(input('Введите количество времени в секундах: '))
print(seconds)

hours = seconds // 3600
minutes = (seconds - hours * 3600) // 60
second = seconds % 60

print(f'{hours}:{minutes}:{second}')
