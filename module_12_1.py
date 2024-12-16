import unittest #  импортируем модуль unittest

class Runner: # берем тестируемый класс "Бегун"
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase): #   создаем класс RunnerTest,
    # который наследуется от unittest.TestCase

    def test_walk(self): # создаем метод test_walk внутри класса RunnerTest
        runner = Runner("Klod") # создаем объект и присваиваем имя
        for _ in range(10): # вызываем метод walk  циклом 10 раз
            runner.walk() # с каждым витком цикла дистанция увеличивается на 5
        self.assertEqual(runner.distance, 50) # проверяем что в итоге дистанция равна 50

    def test_run(self): # аналогично для метода test_run только дистанция увеличивается на 10
        runner = Runner("Piter")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self): # Метод test_challenge создает два объекта -
        # один бегает, второй ходит и проверяет, что их дистанции не равны

        runner1 = Runner("Charlie")
        runner2 = Runner("Diana")

        for _ in range(10): # цикл 10 раз
            runner1.run()
            runner2.walk()

        self.assertNotEqual(runner1.distance, runner2.distance)
        # проверяет что их дистанции не равны


if __name__ == '__main__':
    unittest.main()