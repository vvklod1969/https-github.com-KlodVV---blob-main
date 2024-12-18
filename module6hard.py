import math

# опишем основной класс Figure, который содержит общие атрибуты и методы для всех фигур
class Figure:
    def __init__(self, color, *sides):
        self.__sides = []
        self.__color = list(color)
        self.filled = False

        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count  # Значения по умолчанию

    @property
    def sides_count(self):
        return 0

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def __str__(self):
        return f"Color: {self.__color}, Sides: {self.__sides}"

# создаем класс Circle, наследуетcz от Figure, но добавляет свои уникальные атрибуты и методы.
class Circle(Figure):
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(self.get_sides()) == 1:
            self.__radius = self.get_sides()[0] / (2 * math.pi)  # длина окружности = 2 * pi * r
        else:
            self.__radius = 1  # значение по умолчанию

    # переопределяем свойство sides, чтобы при установке сторон обновлялся радиус
    @property
    def sides(self):
        return self.get_sides()[0]

    @sides.setter
    def sides(self, value):
        self.set_sides(value)
        self.__radius = self.get_sides()[0] / (2 * math.pi)  # обновление радиуса при изменении стороны

    @property
    def sides_count(self):
        return 1

    def get_square(self):
        return math.pi * (self.__radius ** 2)

    def __str__(self):
        return f"Circle - {super().__str__()} , Radius: {self.__radius}, Area: {self.get_square()}"

# создаем класс Triangle, который также наследуется от Figure
class Triangle(Figure):
    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    @property
    def sides_count(self):
        return 3

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

    def __str__(self):
        return f"Triangle - {super().__str__()} , Area: {self.get_square()}"

# создаем класс Cube, который также наследует от Figure
class Cube(Figure):
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(self.get_sides()) == 1:
            self.__sides = [sides[0]] * 12  # 12 одинаковых рёбер
        else:
            self.__sides = [1] * 12  # Значения по умолчанию

    @property
    def sides_count(self):
        return 1

    # Переопределяем свойство sides, чтобы при установке сторон обновлялся размер рёбер
    @property
    def sides(self):
        return self.get_sides()[0]

    @sides.setter
    def sides(self, value):
        self.set_sides(value)
        self.__sides = [value] * 12  # Обновление всех сторон при изменении одной

    def get_volume(self):
        return self.__sides[0] ** 3

    def __str__(self):
        return f"Cube - {super().__str__()} , Volume: {self.get_volume()}"


# Примеры создания объектов с проверкой кол-ва сторон
circle1 = Circle((200, 200, 100), 10)
print(f"Circle1: {circle1}")
circle2 = Circle((200, 200, 100), 10, 15, 6)
print(f"Circle2: {circle2}")  # должно быть [1]

triangle1 = Triangle((200, 200, 100), 10, 6, 7)
print(f"Triangle1: {triangle1}")
triangle2 = Triangle((200, 200, 100), 10, 6)
print(f"Triangle2: {triangle2}")  # должно быть [1, 1, 1]

cube1 = Cube((222, 35, 130), 6)
print(f"Cube1: {cube1}")
cube2 = Cube((222, 35, 130), 6, 12)
print(f"Cube2: {cube2}")  # должно быть [1, 1, ..., 1] (12 шт)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # изменится
print("Circle1 Color:", circle1.get_color())
cube1.set_color(300, 70, 15)  # не изменится
print("Cube1 Color:", cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # не изменится
print("Cube1 Sides:", cube1.get_sides())
circle1.set_sides(15)  # изменится
print("Circle1 Sides:", circle1.get_sides())

# проверка периметра (круга), т.е. его длина:
print("Circle1 Length:", len(circle1))

# проверка объёма (куба):
print("Cube1 Volume:", cube1.get_volume())

# Дополнительные тесты
print("\n--- Дополнительные тесты ---")

# проверка изменения радиуса при изменении сторон круга
print("Initial Circle Radius:", circle1._Circle__radius)
circle1.sides = 20
print("Updated Circle Radius:", circle1._Circle__radius)
print(f"Updated Circle1: {circle1}")

# проверка изменения ребра при изменении сторон куба
print("Initial Cube Sides:", cube1.get_sides())
cube1.sides = 10
print("Updated Cube Sides:", cube1.get_sides())
print(f"Updated Cube1: {cube1}")

# проверка на создание объектов с некорректными данными
invalid_circle = Circle((100, 150, 200), 10, 15)
print(f"Invalid Circle: {invalid_circle}")

invalid_triangle = Triangle((100, 150, 200), 5)
print(f"Invalid Triangle: {invalid_triangle}")

invalid_cube = Cube((100, 150, 200), 5, 10)
print(f"Invalid Cube: {invalid_cube}")