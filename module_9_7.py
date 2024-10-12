print(f'Задача - "Декораторы"')
# Функция декоратор (is_prime), выводит "Простое",
# если результат 1ой функции будет простым числом, а  в противном случае - "Составное" .
def is_prime(func):
    # внутренняя функция wrapper в is_prime
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        sum_ = sum(args)
        k = 0
        for i in range(2, sum_ // 2 + 1):
            if sum_ % i == 0:
                k = k + 1
        if k <= 0:
            print('Простое')
        else:
            print('Составное')
        return result

    return wrapper

@is_prime  # @is_prime - декоратор для функции sum_three
def sum_three(*args):  # Функция, которая складывает 3 числа (sum_three)
    return sum(args)

result = sum_three(2, 3, 6)
print(result)
