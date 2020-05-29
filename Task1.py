''' Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
и метод running (запуск). Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый)
— 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
'''
import time

class TrafficLight:
    def __init__(self, traffic_color):
        self.color = traffic_color
        self._running()
        # self.__running = 'Красный', 'Желтый', 'Зелёный'

    def _running(self):
        while True:
            print('Красный')
            time.sleep(7)
            print('Желтый')
            time.sleep(2)
            print('Зелёный')
            time.sleep(5)

my_light = TrafficLight('')
# print(my_light._TrafficLight__running)

# print(my_light1.color)
# my_light2 = TrafficLight('желтый')
# print(my_light2.color)
# my_light3 = TrafficLight('зеленый')
# print(my_light3.color)
