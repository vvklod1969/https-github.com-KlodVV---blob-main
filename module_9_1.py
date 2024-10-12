print (f'Задача "вызов разом"')
def apply_all_func(int_list, *functions):
# Данная функция возвращает словарь с ключом названия функции и значением результата функции
#int_list - список из чисел (int, float)
#*functions - неограниченное количество функций для списка
    results = {}
    for func in functions:
        results[func.__name__] = func(int_list)
    return results


if __name__ == '__main__':
    print(apply_all_func([6, 20, 15, 9], max, min))
    print(apply_all_func([6, 20, 15, 9], len, sum, sorted))