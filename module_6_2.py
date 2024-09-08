print(f'Задана - "Изменять нельзя получать"')
class Vehicle: # - это любой транспорт
    __COLOR_VARIANTS = ['красный', 'темная ночь', 'фиолетовый металик', 'серый', 'молочный']  # атрибут класса

    def __init__(self, owner, __model, __color, __engine_power):  # атрибуты объекта
        self.owner: str = owner # владелец, который может измениться
        self.__model: str = __model # модель - неизменяемый атрибут
        self.__engine_power: int = __engine_power #  мощность двигателя - неизменяемый атрибут
        self.__color: str = __color # цвет - неизменяемый атрибут

    def get_model (self) :
        return f'"Модель: {self.__model}'

    def get_horsepower (self) :
        return f'"Мощность двигателя: {self.__engine_power}'

    def get_color (self) :
        return f'"Цвет: {self.__color}'
    def print_info (self):
        print(self.get_model())
        print(self.get_horsepower ())
        print(self.get_color())
        print(f'Владелец : {self.owner}')

    def set_color (self, new_color:str):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print (f'"Нельзя сменить цвет на {new_color}')

class Sedan (Vehicle): # класс Седан дочерний от класса Vehicle
    __PASSENGERS_LIMIT = 5 # атрибут класса Седан - в седан может поместиться не более 5 пассажиров

# Текущие цвета __COLOR_VARIANTS = ['красный', 'темная ночь', 'фиолетовый металик', 'серый', 'молочный']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
print()

vehicle2 = Sedan('Андрей', 'Лада Калина', 'голубая лагуна', 500)
vehicle2.print_info()
vehicle2.set_color('белый')
vehicle2.set_color('фиолетовый металик')
vehicle2.set_color('черный')
vehicle2.owner = 'Ирина'
vehicle2.print_info()