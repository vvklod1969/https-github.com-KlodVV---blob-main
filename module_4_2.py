print(f'Задача: "Пространство имен"')
def test_function ():
    def inner_function ():
        print("Я в области видимости функции inner_function")
        

    inner_function()
test_function()
