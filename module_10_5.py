import datetime
import multiprocessing
import os

def read_info(name):
    """Функция читает строки из файла и сохраняет их в all_data,
    но не возвращает этот список, так как это не требуется по условию."""
    all_data = []
    with open(name, 'r') as file:
        line = file.readline()
        while line != '':
            all_data.append(line)
            line = file.readline()
   
# Список имен файлов
filenames = [rf'C:\Users\user\Documents\GitHub\Учеба\module10\file {number}.txt' for number in range(1, 5)]


# Линейный вызов
start_l = datetime.datetime.now()
for name_file in filenames:
    read_info(name_file)
end_l = datetime.datetime.now()
result_linear = end_l - start_l
print(f'{result_linear} - (линейный)')

# Многопроцессный вызов
if __name__ == '__main__':
    """ Эта конструкция гарантирует, что код, связанный с многопроцессностью, 
    будет выполняться только в случае, если скрипт запускается как основная программа. """
    with multiprocessing.Pool(processes=4) as pool:
        start_mp = datetime.datetime.now()
        pool.map(read_info, filenames)
        end_mp = datetime.datetime.now()
        result_multiprocess = end_mp - start_mp
        print(f'{result_multiprocess} - (многопроцессный)')
