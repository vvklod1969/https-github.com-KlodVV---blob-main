my_dict = {"Владимир": 54,"Иван": 60, "Сергей": 25, "Ирина" : 31, "Лариса": 43}
print(my_dict)
print(my_dict["Ирина"])
print(my_dict.get("Петр", "Такого имени в списке нет!"))
my_dict.update ({"Петр": 71, "Филимон" : 14})
print(my_dict)
a = my_dict.pop("Лариса")
print(my_dict)
print(a)
print(my_dict)
# Работа с множествами
print("Работа с МНОЖЕСТВАМИ")
my_set = {1,2,3,4,"Ирина", 12.5, 3,4,5,6,7,"Федор",True, 2,1}
print(my_set)
my_set.add(78)
my_set.add("Калигула")
print(my_set)
my_set.discard(6)
print(my_set)