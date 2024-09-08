print(f'Задача - "Мифическое наследование"')

class Horse: #класс описывающий лошадь.
    def __init__(self):
        super().__init__()
        self.x_distance = 0 # - пройденный путь лошадью.
        self.sound = 'Frrr' # - звук, который издаёт лошадь.
    def run(self, dx):
        self.x_distance += dx # - изменение дистанции, увеличивает x_distance на dx.
        return self.x_distance

class Eagle: # - класс описывающий орла.
    def __init__(self):
        super().__init__()
        self.y_distance = 0 # - высота полёта
        self.sound = 'I train, eat, sleep, and repeat' # - звук, который издаёт орёл

    def fly(self, dy):
        self.y_distance += dy # - изменение дистанции орла, увеличивает y_distance на dy.
        return self.y_distance

class Pegasus (Horse, Eagle): # - класс описывающий пегаса. Наследуется от Horse и Eagle.
    def __init__(self):
        super().__init__()
        Eagle.__init__(self)


    def move(self, dx, dy): # - где dx и dy изменения дистанции.
        return self.fly(dy), self.run(dx)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice (self):
       print (self.sound)

p1 = Pegasus()
print(p1.get_pos())
print()
p1.move(10, 15)
print(p1.get_pos())
print()
p1.move(-5, 20)
print(p1.get_pos())
print()
p1.voice()


print(Pegasus.mro())
