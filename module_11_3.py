
'''Создание функции introspection_info(obj)'''

import inspect

def introspection_info(obj):
    """
    Функция для интроспекции объекта и получения информации о нем.
    Args: obj: Объект любого типа, который нужно исследовать.
    Returns: dict: Словарь с информацией об объекте
    """
    info = {}
    info['type'] = str(type(obj)) # определение объекта
    # Получение атрибутов объекта
    attributes = []
    for name in dir(obj):
        if not name.startswith('__'):
            try:
                attr = getattr(obj, name)
                attributes.append(f"{name}: {attr}")
            except Exception:
                attributes.append(f"{name}: <Недоступно>")
    info['attributes'] = attributes
    # Получение медодов объекта
    methods = []
    for name in dir(obj):
        if callable(getattr(obj, name)):
            if not name.startswith('__'):
                methods.append(name)
    info['methods'] = methods
    #Получение модуля объекта
    if hasattr(obj, '__module__'):
        info['module'] = obj.__module__
    else:
        info['module'] = None
    # Добавление дополнительных свойств
    if isinstance(obj, int):
        info['is_positive'] = obj > 0
    elif isinstance(obj, str):
        info['length'] = len(obj)
    elif inspect.isclass(obj):
        info['bases'] = [base.__name__ for base in obj.__bases__]

    return info # возвращаем словарь

'''Создаем свой класс'''
class MyClass:
    def __init__(self, value):
        self.value = value

    def my_method(self):
        return f"Значение: {self.value}"

    @property
    def my_property(self):
        return self.value * 2


# Создание объектов разных типов для тестирования
number = 42
string = "Hello, world!"
my_object = MyClass(10)
my_class = MyClass

# Вызов функции и вывод результатов
number_info = introspection_info(number)
print("Информация о числе:", number_info)
print("-" * 30)

string_info = introspection_info(string)
print("Информация о строке:", string_info)
print("-" * 30)

object_info = introspection_info(my_object)
print("Информация о созданном объекте:", object_info)
print("-" * 30)

class_info = introspection_info(my_class)
print("Информация о созданном классе:", class_info)