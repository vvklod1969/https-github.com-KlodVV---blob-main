def add_everything_up(arg1, arg2):
    try:
        result = arg1 + arg2
        print('Наш результат -', round(result,3))
    except TypeError:
        result = str(arg1) + str(arg2)
        print(" У нас разные типы данных !!! Поэтому получаем : " ,  result)
    return result

add_everything_up(123.456, 'строка')
add_everything_up('яблоко', 4215)
add_everything_up(123.456, 7)
