import threading
import random
import time
from threading import Thread, Lock

print(f'Задача - "Банковские операции"')
# Создаем класс Bank со следующими свойствами:
# Атрибуты объекта:
# balance - баланс банка (int)
# lock - объект класса Lock для блокировки потоков.
class Bank(Thread):
    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = Lock()

# Метод deposit: совершает 100 транзакций пополнения средств на случайное число от 50 до 500.
# Если баланс больше или равен 500 и замок lock заблокирован - то разблокировать его
# После увеличения баланса выводится строка -
# "Пополнение: <случайное число>. Баланс: <текущий баланс>".
# После всех операций предусмотреть ожидание в 0.001 сек. имитируя скорость выполнения транзакции.
    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            y = random.randint(50, 500)
            self.balance += y
            print(f'Произошло пополнение банаса на : {y} единиц. Ваш баланс: {self.balance}')
            time.sleep(0.001)

            # Метод take: совершает 100 транзакций снятия, т.е. уменьшение баланса на
            # случайное целое число от 50 до 500.
            # Предварительно должно выводится сообщение "Запрос на снятие <случайное число>".
            # Далее производится проверка: если случайное число меньше или равно текущему балансу,
            # то произвести снятие, путем уменьшения balance на соответствующее число с выводом
            # "Снятие: <случайное число>. Баланс: <текущий баланс>".
            # Если случайное число оказалось больше баланса, то вывести строку
            # "Запрос отклонён, недостаточно средств" и заблокировать поток.
    def take(self):
        for i in range(100):
            x = random.randint(50,500)
            print(f'Поступил запрос на снятие {x} единиц')
            if self.balance >= x:
                self.balance -= x
                print(f'Произведено снятие: {x} единиц. Ваш баланс: {self.balance}')
            else:
                print(f'Запрос на сятие отклонён, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)


bk = Bank() # создаем объект класса Bank
# Создаем 2 потока для его методов deposit и take.

t1 = threading.Thread(target=Bank.deposit, args=(bk,))
t2 = threading.Thread(target=Bank.take, args=(bk,))
#  Запускаем потоки.
t1.start()
t2.start()
t1.join()
t2.join()

print(f'Ваш итоговый баланс: {bk.balance}')