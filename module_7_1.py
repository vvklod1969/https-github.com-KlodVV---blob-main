print(f'Задача - "Учёт товаров"')
from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        str_product = f'{self.name}, {self.weight}, {self.category}'
        return str_product

class Shop:
    __file_name = 'product.txt'
    def get_product(self):
        file = open(self.__file_name,'r+')
        prod_str = file.read()
        file.close()
        return prod_str

    def add(self, *products):
        self.get_product()
        for i in products:
            if self.get_product().find(f'{i.name},') == -1:
                file = open(self.__file_name, 'a')
                file.write(f'{i}\n')
                file.close()
            else:
                print(f'Продукт {i.name} уже есть в магазине')


s1 = Shop()
p1 = Product('Картофель', 50.5, 'Овощи')
p2 = Product('Макароны', 3.4, 'Продукты')
p3 = Product('Картофель', 5.5, 'Овощи')
p4 = Product('Яблоки', 67.6, 'фрукты')
print(p2)
s1.add(p1, p2, p3, p4)
print(s1.get_product())

