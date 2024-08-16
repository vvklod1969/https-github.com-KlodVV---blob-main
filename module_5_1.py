print(f'Задача: " Developer - не только разработчик"')
class Haus:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        #self.go_to(new_floor)

    def go_to(self, new_floor):
        print(self.name)
        if 0 < new_floor <= self.number_of_floors:
            for floor in range (1, new_floor +1):
                print("Возможный этаж - ", floor)
        else:
            print("Такого этажа не существует")


D1 = Haus ('ЖК Горский', 18)
D2 = Haus ('Домик в деревне', 2)
D1.go_to(5)
D2.go_to(3)


