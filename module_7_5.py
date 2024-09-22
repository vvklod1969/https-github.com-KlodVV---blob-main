print(f'Задача - ""Файлы в операционной системе"')
import os
import time

#Научиться применять методы os.walk, os.path.join, os.path.getmtime,
# os.path.dirname, os.path.getsize и модуля time для корректного отображения времени.

#Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
#Примените os.path.join для формирования полного пути к файлам.
#Используйте os.path.dirname для получения родительской директории файла.


#Чтобы обойти каталог, путь к которому указывает переменная directory,
# и сформировать полный путь к файлам, можно использовать следующий код:

#Импортируйте модуль os и переберите кортежи, которые возвращает функция os.walk(directory):
# for path, folders, files in os.walk(directory).
# Для каждого файла в списке files откройте его с помощью os.path.join(directory, имя файла).
#Для получения времени последнего изменения файла и его размера можно использовать функции модуля os.path:
#os.path.getmtime(path);
#os.path.getsize(path).
#Чтобы получить родительскую директорию пути path, можно использовать функцию
# os.path.dirname(path).

directory = "."
print(os.getcwd())
path = os.getcwd()

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: '
            f'{formatted_time}, Родительская директория: {parent_dir}')

