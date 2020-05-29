'''Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
создать экземпляры класса Position, передать данные, проверить значения атрибутов,
вызвать методы экземпляров).
'''
class Worker():
    def __init__(self, name, surname, income, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):

    def get_full_name(self):
        print(f'Name: {self.name} \nSurname: {self.surname}\nPosition: {self.position}')

    def get_total_income(self):
        total_income = self._income['wage'] + self._income['bonus']
        print(total_income)


worker_1 = Position('Max', 'Ivanovski', {'wage': 50000, 'bonus': 4000}, 'mechanic')
worker_1.get_full_name()
worker_1.get_total_income()

worker_2 = Position('Alex', 'Rubanov', {'wage': 80000, 'bonus': 15000}, 'teacher')
worker_2.get_full_name()
worker_2.get_total_income()
