'''== Лото ==

Правила игры в лото.

Игра ведется с помощью спе циальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html '''
import random

class LotoGame:

    def __init__(self, player, computer):
        self._player = player
        self._computer = computer
        self._numbers_count = 90
        max_number = 90
        self._numbers_in_bag = random.sample(range(1, max_number + 1), self._numbers_count)

    def _get_number(self):
        return self._numbers_in_bag.pop()

    def start(self):
        for _ in range(self._numbers_count):
            print(self._player, self._computer)
            number = self._get_number()
            print('Новый бочонок {}, осталось {}'.format(number, len(self._numbers_in_bag)))
            choice = input('Хотите зачеркуть? y/n:\n')
            if choice == 'y':
                if not self._player.try_stroke_number(number):
                    print('Игрок проиграл!')
                    break
            elif self._player.has_number(number):
                print('Игрок проиграл!')
                break
            if self._computer.has_number(number):
                self._computer.try_stroke_number(number)

class LotoCard:
    def __init__(self, player_type):
        self.player_type = player_type
        self._card = [[],
                      [],
                      []]
        self._max_number = 90
        self._max_numbers_in_card = 15
        self._numbers_stroked = 0
        interval = 4
        numbers = 5
        self._numbers = random.sample(range(1, self._max_number + 1), self._max_numbers_in_card)

        for line in self._card:
            for _ in range(interval):
                line.append(' ')
            for _ in range(numbers):
                line.append(self._numbers.pop())

        def check_sort_item(item):
            if isinstance(item, int):
                return item
            return random.randint(1, self._max_number)

        for index, line in enumerate(self._card):
            self._card[index] = sorted(line, key=check_sort_item)

    def has_number(self, number):
        for line in self._card:
            if number in line:
                return True
        return False

    def try_stroke_number(self, number):
        for index, line in enumerate(self._card):
            for num_index, number_in_card in enumerate(line):
                if number == number_in_card:
                    self._card[index][num_index] = '-'
                    self._numbers_stroked += 1
                    if self._numbers_stroked >= self._max_numbers_in_card:
                        raise Exception('{} победил!'.format(self.player_type))
                    return True
        return False

    def __str__(self):
        max_field_length = 3
        header = '\n{}:\n--------------------------'.format(self.player_type)
        body = '\n'
        for line in self._card:
            for field in line:
                body += str(field).ljust(max_field_length)
            body += '\n'
        return header + body

human_player = LotoCard('Игрок')
computer_player = LotoCard('Компьютер')

game = LotoGame(human_player, computer_player)
game.start()
