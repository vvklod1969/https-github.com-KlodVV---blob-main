print(f'Задача - "Создание генераторных сборок"')

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
#Для первой сборки (first_result) создаем генераторную сборку,
# которая высчитывает разницу длин строк из списков first и second, если они не равны.
# Для перебора строк  используем функцию zip()
first_result = (len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y))
# Для второй сборки (second_result) создаем генераторную сборку,
# которая сравнивает длины строк в одинаковых позициях из списков first и second.
# Для этого используем функции range и len.
second_result = ((len(first[x]) == len(second[x])) for x in range(len(first)))


print(list(first_result))
print(list(second_result))

