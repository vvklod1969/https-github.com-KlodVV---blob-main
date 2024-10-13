print(f'Задача - "Потоки гостей в кафе"')

import time
from threading import Thread
import queue
from random import randint
# вносим список ожидаемых гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman', 'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya',
    'Alexandra']

#  Создаем класс Table - номер стола, и есть ли за ним гость (Guest)
class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

# Создаем класс Guest - имя гостя, поток, при запуске которого происходит задержка от 3 до 10 сек.
class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(randint(3, 10))

# Создаем класс Cafe - кафе, в котором есть определённое кол-во столов,
# прибывают гости (guest_arrival) и происходит их обслуживания (discuss_guests).
class Cafe:
    def __init__(self, *tables):
        self.queue = queue.Queue()
        self.tables = tables

    def guest_arrival(self, guest): #  guest_arrival обрабатывает одного гостя за раз.
        for table in self.tables:
            if table.guest is None:
                table.guest = guest
                guest.start()  # Запуск потока для гостя
                return guest.name, table.number
        self.queue.put(guest)
        return guest.name, None

    def discuss_guests(self):
        for table in self.tables:
            if table.guest is not None and not table.guest.is_alive():
                print(f'Гость {table.guest.name} покушал(-а) и ушёл(ушла)')
                print(f'Стол номер {table.number} свободен')
                table.guest = None
                if not self.queue.empty():
                    next_guest = self.queue.get()
                    table.guest = next_guest
                    next_guest.start()
                    print(f'Гость {next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Создание столов
tables = [Table(number) for number in range(1, 6)]
cafe = Cafe(*tables)

# Прибытие гостей
for guest in guests:
    name, table_number = cafe.guest_arrival(guest)
    if table_number:
        print(f'Гость {name} сел(-а) за стол номер {table_number}')
    else:
        print(f'Гость {name} встал(-а) в очередь')

# Обсуждение гостей - цикл, который продолжает обсуждение гостей, пока есть занятые столы или гости в очереди.
while any(table.guest is not None for table in tables) or not cafe.queue.empty():
    cafe.discuss_guests()
    time.sleep(1)



