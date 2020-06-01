'''Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда,
которая может иметь определенное название. К типам одежды в этом проекте
относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике
работу декоратора @property.'''
from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def my_method_1(self):
        print('Тип одежды: ', end='')

    @abstractmethod
    def my_method_2(self):
        print('Параметры одежды: ', end='')

    @abstractmethod
    def my_method_3(self):
        print('Расход ткани: ', end='')

class Coat(Clothes):
    def my_method_1(self):
        super().my_method_1()
        print('Пальто')

    def my_method_2(self):
        super().my_method_2()
        print('Размер')

    def my_method_3(self):
        super().my_method_3()
        return float(self.value) / 6.5 + 0.5


class Suit(Clothes):
    def my_method_1(self):
        super().my_method_1()
        print('Костюм')

    def my_method_2(self):
        super().my_method_2()
        print('Рост')

    def my_method_3(self):
        super().my_method_3()
        return 2 * float(self.value) + 0.3


class Total:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def sum(self):
        return (self.size / 6.5 + 0.5) + (2 * self.height + 0.3)


size_coat = 40
size_suit = 46

coat = Coat(size_coat)
coat.my_method_1()
coat.my_method_2()
print('%.2f' % coat.my_method_3())

suit = Suit(size_suit)
suit.my_method_1()
suit.my_method_2()
print('%.2f' % suit.my_method_3())

total = Total(size_coat, size_suit)
print('\nОбщий расход ткани: %.2f' % total.sum())
