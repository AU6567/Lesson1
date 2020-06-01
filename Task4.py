'''Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево).  А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость
автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение
о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''
class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        self.direction = direction
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость {self.speed} km/h')
        if self.speed > 60:
            print('Скорость превышена! Сбросьте скорость! Разрешенная скорость 60 km/h!')


class TownCar(Car):
    def show_speed(self):
        print(f'Текущая скорость {self.speed} km/h')
        if self.speed > 60:
            print('Скорость превышена! Сбросьте скорость! Разрешенная скорость 60 km/h!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'Текущая скорость {self.speed} km/h')
        if self.speed > 40:
            print('Скорость превышена! Сбросьте скорость! Разрешенная скорость 40 km/h!')


class PoliceCar(Car):
    pass

town_car = TownCar(65, 'черный', 'BMW 320i', False)
print(f'Городской автомобиль {town_car.name}')
print(f'Цвет - {town_car.color}')
print(f'Это полицейская машина: {town_car.is_police}')
town_car.go()
town_car.show_speed()
town_car.turn('направо')
town_car.stop()

sport_car = SportCar(130, 'салатовый', 'Lamborghini', False)
print(f'Спорткар {sport_car.name}')
print(f'Цвет - {sport_car.color}')
print(f'Это полицейская машина: {sport_car.is_police}')
sport_car.go()
sport_car.show_speed()
sport_car.turn('налево')
sport_car.stop()

work_car = WorkCar(41, 'синий', 'Reno Duster', False)
print(f'Рабочая машина {work_car.name}')
print(f'Цвет - {work_car.color}')
print(f'Это полицейская машина: {work_car.is_police}')
work_car.go()
work_car.show_speed()
work_car.turn('назад')
work_car.stop()

police_car = PoliceCar(240, 'белый', 'Nissan Almera', True)
print(f'Полицейская машина {police_car.name}')
print(f'Цвет - {police_car.color}')
print(f'Это полицейская машина: {police_car.is_police}')
police_car.go()
police_car.show_speed()
police_car.turn('в обратную сторону')
police_car.stop()


# class Car():
#     def __init__(self, speed, color, name, is_police):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#
#     def go(self):
#         print('Машина поехала')
#
#     def stop(self):
#         print('Машина остановилась')
#
#     def turn(self, direction):
#         self.direction = direction
#         print('Машина повернула {direction}')
#
#     def show_speed(self):
#         print(f'Текущая скорость {self.speed} km/h')
#         if self.speed > 60:
#             print('Скорость превышена!')
#
# class TownCar(Car):
#     def __init__(self, speed, color, name, is_police, show_speed):
#         super().__init__(speed, color, name, is_police, show_speed)
#
#     def show_speed(self):
#         print(f'Текущая скорость {self.speed} km/h')
#         if self.speed > 60:
#             print('Скорость превышена!')
#
# class SportCar(Car):
#     pass
#
# class WorkCar(Car):
#     def __init__(self, speed, color, name, is_police, show_speed):
#         super().__init__(speed, color, name, is_police, show_speed)
#         print(f'Текущая скорость {self.speed} km/h')
#
#     def show_speed(self):
#         if self.speed > 40:
#             print('Скорость превышена!')
#
# class PoliceCar(Car):
#     pass
#
