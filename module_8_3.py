print(f'Задача "Некорректность"')
# Создаем класс исключений IncorrectVinNumber
class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message
        print(self.message)

# Создаем классы исключений:
# Класс - IncorrectCarNumbers
class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message
        print(self.message)

# Класс Car
class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        if self.__is_valid_vin(vin) and self.__is_valid_numbers(numbers):
            self.__vin = vin
            self.__numbers = numbers
            print(f'{self.model} успешно создан')
        else:
            pass
# Используемый метод __is_valid_vin(vin_number) - принимает vin_number и проверяет его на корректность.
    def __is_valid_vin(self, vin_number):
        try:
            if isinstance(vin_number, float):
                raise IncorrectVinNumber('Некорректный тип vin номерa')
            if not 1000000 <= vin_number <= 9999999:
                raise IncorrectVinNumber('Неверный диапазон для vin номера')
        except IncorrectVinNumber:
            pass
        else:
            return True


# Используемый метод __is_valid_numbers(numbers) - принимает numbers и проверяет его на корректность.
    def __is_valid_numbers(self, numbers):
        try:
            if not isinstance(numbers, str):
                raise IncorrectCarNumbers('Некорректный тип данных для номеров')
            if len(numbers) != 6:
                raise IncorrectCarNumbers('Неверная длина номера')
        except IncorrectCarNumbers:
            pass
        else:
            return True

# Проверяем

car1 = Car('Мазда CX-5', 5565657, 'А222ОА')
car2 = Car('БМВ X52', 3333, 'О222ОО')
car3 = Car('Лада Веста', 5555555.7, 'У222УО')
car4 = Car('Мазда 3', 1234567, 'Х567ОУ')
car5 = Car('Омода', 7777777, 'Е58лл37')
car6 = Car('Лексус 330', 85.25, 'В9О9ВВ')