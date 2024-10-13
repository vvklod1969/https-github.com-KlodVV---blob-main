print(f'Задача - "Потоковая запись в файлы"')
import time
from datetime import datetime
from time import sleep
from threading import Thread

def write_words(word_count, file_name): # задаем функцию записи слов в соответствующий файл
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f"Какое-то слово № {i}\n")
            time.sleep(0.1)
    file.close()
    print(f'Завершилась запись в файл {file_name}')

time_start1 = datetime.now() # Взятие текущего времени

# Запуск функций с аргументами из задачи

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

# Определение и вывод времени, затраченного на выполнение задачи
time_stop1 = datetime.now()
time_res1 = time_stop1 - time_start1
sec1 = time_res1.total_seconds()

print(f'Время работы функций {sec1} секунды')

time_start2 = datetime.now() # засекаем время начала работы потоков
# Создаем 4 потока
the_p1 = Thread(target=write_words, args=(10, "example5.txt"))
the_p2 = Thread(target=write_words, args=(30, "example6.txt"))
the_p3 = Thread(target=write_words, args=(200, "example7.txt"))
the_p4 = Thread(target=write_words, args=(100, "example8.txt"))

# запускаем потоки
the_p1.start()
the_p2.start()
the_p3.start()
the_p4.start()

# заканчиваем работу потоков
the_p1.join()
the_p2.join()
the_p3.join()
the_p4.join()

time_end2 = datetime.now() # засекаем время окончания работы потоков

# высчитываем и выводим время работы потоков
time_res2 = time_end2 - time_start2
sec2 = time_res2.total_seconds()
print(f'Время работы функций в потоке {sec2} секунды, что на {sec1 - sec2} секунды быстрее')



