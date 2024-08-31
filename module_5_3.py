print(f'Задача: " Нужно больше этажей"')
class Haus:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        print(self.name)
        if 0 < new_floor <= self.number_of_floors:
          for floor in range (1, new_floor +1):
             print("Возможный этаж - ", floor)
        else:
             print("Такого этажа не существует")

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
       return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self
    def __iadd__(self,value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self
    def __radd__(self, value):
        if isinstance(value, int):
            self.number_of_floors = value + self.number_of_floors
        return self
    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors
    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors
    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors


print()
print("Выполняется 1 задание!")
print()
D1 = Haus ('ЖК "Горский"', 18)
D2 = Haus ('ЖК "Домик в деревне"', 2)
D1.go_to(5)
D2.go_to(3)
print()
print(f'выполняется 2 задание!')
print()
h1 = Haus('Сочи, "ЖК Монту-Карло"', 21)
h2 = Haus('Москва, "ЖК Лучи"', 14)
print(h1)
print(h2)
print(len(h1))
print(len(h2))
print()
print(f'выполняется 3 задание')
print()
h1 = Haus('ЖК Эльбрус', 10)
h2 = Haus ('ЖК Акация', 20)
print(h1)
print(h2)
print(h1 == h2) # __eq__
#h2.number_of_floors = 10
#print(h1 == h2) # __eq__
print()
h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)
print()
h1 += 10
print(h1)
print()
h2 = 10 + h2 # __radd__
print(h2)
print()
print(h1>h2) # __gt__
print()
print(h1 >= h2) # __ge__
print()
print(h1<h2) # __lt__
print()
print(h1<=h2) # __le__
print()
print(h1!=h2) # __ne__

