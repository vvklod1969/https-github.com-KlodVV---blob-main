print(f'Задача -\"Все ли числа равны?"')
print("Ввведите 3 любых целых числа: ")
first = int(input('Введите первое число : '))
second = int(input('Ведите второе число: '))
third = int(input('Ведите третье  число: '))
if first == second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else: print(0)
