'''Реализовать класс Road (дорога), в котором определить атрибуты: length (длина),
width (ширина). Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина*ширина*масса асфальта для покрытия
одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
'''
class Road:
    def __init__(self, _length, _width, weight, thickness):
        self._length = _length
        self._width = _width
        self.weight = weight
        self.thickness = thickness

    def mass(self):
        leng = self._length
        wid = self._width
        weig = self.weight
        thic = self.thickness
        total = leng * wid * weig * thic / 1000
        return print(f'\n {leng}м*{wid}м*{weig}кг*{thic}см = ', int(total), 'т')

my_road = Road(20, 5000, 25, 5)
my_road.mass()
