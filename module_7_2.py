print(f'Задача - "Записать и запомнить"')
from pprint import pprint


# Создайте функцию custom_write(file_name, strings), которая принимает аргументы
# file_name - название файла для записи, strings - список строк для записи.
# Функция должна:
# Записывать в файл file_name все строки из списка strings, каждая на новой строке.
# Возвращать словарь strings_positions,
# где ключом будет кортеж (<номер строки>, <байт начала строки>), а значением - записываемая строка.
# Для получения номера байта начала строки используйте метод tell() перед записью.

def custom_write(file_name, strings):
    strings_positions = {}

    file = open(file_name, 'w', encoding='utf-8')
    for p, s in enumerate(strings):
        key = (p + 1, file.tell())
        strings_positions[key] = s
        file.write(s + '\n')
        # Для записи файла в Python используется функция write().
        # В качестве аргумента ей следует передать строку, содержимое которой будет записано
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]
result = custom_write('TestFail.txt', info)
for elem in result.items():
    print(elem)
