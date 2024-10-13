print(f'Задача - "За честь и отвагу!"')
import time
from datetime import datetime
from time import sleep
from threading import Thread

time_start = datetime.now()
#Создаем класс рыцаря (Knight), наследованный от Thread,
# объекты класса бладают следующими свойствами:
# Атрибут name - имя рыцаря (str)
# Атрибут power - сила рыцаря (int)
class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemy = 100

# Определяем метод run, в котором рыцарь будет сражаться с врагами (в каждом потоке их 100).
# При запуске потока выводим надпись "<Имя рыцаря>, на нас напали!".
# Рыцарь сражается до тех пор, пока всех не победит.
# В процессе сражения количество врагов уменьшается на power текущего рыцаря.
# По прошествию 1 дня сражения(1 секунды) выводится строка "<Имя рыцаря> сражается <кол-во дней>...,
# осталось < кол - во врагов > врагов."
# После  победы над всеми врагами выводим "<Имя рыцаря> одержал победу спустя <кол-во дней> дней(дня)!"
    def run(self):
        print(f'Рыцарь {self.name} на нас напали!')
        day = 1
        self.enemy -= self.power
        while self.enemy > 0:
            print(f'Рыцарь {self.name}, сражается {day} день, осталось {self.enemy} врагов')
            day += 1
            self.enemy -= self.power
            time.sleep(1)
        print(f' Рыцарь {self.name} одержал победу спустя {day} дней!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

time_end = datetime.now()
res = time_end - time_start
sec = res.total_seconds()

print(f'За {sec} секунднд все битвы завершились!')