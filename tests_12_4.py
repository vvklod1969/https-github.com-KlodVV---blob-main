import unittest
import logging
import sys

# осушествляем логгирование
logging.basicConfig(
    level=logging.INFO,  # определяем минимальный уровень логирования
    filemode='w',        # открываем файл в режиме записи, перезаписывая его при каждом запуске
    filename='runner_tests.log',  # задаем имя файла для логов
    encoding='utf-8',   # кодировка файла
    format='%(levelname)s: %(message)s'  # определяем формат сообщения в логе
)


# Класс бегун:
class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):  # проверяем, что имя - это строка
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0  # задаем начальную дистанцию для бегуна
        if speed > 0:      # проверяем, что скорость положительная
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2  # увеличиваем дистанцию на удвоенную скорость

    def walk(self):
        self.distance += self.speed     # увеличиваем дистанцию на скорость

    def __str__(self):
        return self.name                # возвращаем имя бегуна при str()

    def __repr__(self):
        return self.name                # возвращаем имя бегуна при repr()

    def __eq__(self, other):
        if isinstance(other, str):      # если сравниваем с строкой, то сравниваем имя
            return self.name == other
        return isinstance(other, Runner) and self.name == other.name # Если сравниваем с Runner, то сравниваем имена. Если что-то другое - возвращаем False


# Класс Турнир:
class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance   # дистанция для турнира
        self.participants = list(participants)  # список участников турнира

    def start(self):
        finishers = {}  # словарь для хранения финишировавших участников
        place = 1       # текущее место
        while self.participants:    # пока не кончатся все участники в турнире
            for participant in self.participants:
                participant.run()   # бегун пробегает дистанцию
                if participant.distance >= self.full_distance:
                    finishers[place] = participant   # добавляем финишировавшего бегуна в словарь
                    place += 1                      # увеличиваем место
                    self.participants.remove(participant)   # удаляем финишировавшего бегуна из списка
        return finishers     # возвращаем словарь с финишировавшими бегунами

# Функция для пропуска тестов :
def skip_if_frozen(func):
    def wrapper(*args, **kwargs):
        if getattr(sys, 'frozen', False):  # проверяем, заморожено ли приложение
            logging.info(f"Skipping test '{func.__name__}' because the app is frozen.") # логируем пропуск теста
            return unittest.skip("Skipping because the app is frozen.")(lambda: None)() # пропускаем тест
        return func(*args, **kwargs) # вызываем исходный тест, если приложение не заморожено
    return wrapper


# Класс RunnerTest: тесты для класса Runner
class RunnerTest(unittest.TestCase):
    is_frozen = False  # флаг для проверки заморозки приложения

    @skip_if_frozen  # используем декоратор для пропуска теста, если приложение заморожено
    def test_run(self):  # тест для проверки исключения при неверном типе имени
         try:  # делаем попытку создать объект Runner с нестроковым именем
            Runner(123)
            logging.info('"test_run" выполнен успешно') # если исключения нет то логируем успешное выполнение
            self.fail("TypeError was not raised as expected") # сообщаем об ошибке, если исключение не сработало
         except TypeError as e: # ловим TypeError, когда создаем Runner c некорректным именем
            logging.warning(f"Неверный тип данных для объекта Runner: {e}") # логируем ошибку TypeError
            self.assertTrue(True) # убеждаемся, что  тест пройден - исключение поймано

# Аналогично для проверки исключения при неверной скорости
    @skip_if_frozen
    def test_walk(self):
        try:
            Runner("Test", -2)
            logging.info('"test_walk" выполнен успешно')
            self.fail("ValueError was not raised as expected")
        except ValueError as e:
            logging.warning(f"Неверная скорость для Runner: {e}")
            self.assertTrue(True)

    @skip_if_frozen  # используем декоратор для пропуска теста, если приложение заморожено
    def test_challenge(self): #  тест для демонстрации skip_if_frozen
        self.assertTrue(True) # проверяем, что значение истинно

    @classmethod # метод класса, который  всегда выполняется
    def class_method(cls):
        print('this class method should be executed always')

    def test_runner_initialization_valid(self): # тест для правильной инициализации Runner
        runner = Runner("Alice", 7)
        self.assertEqual(runner.name, "Alice")
        self.assertEqual(runner.speed, 7)
        self.assertEqual(runner.distance, 0)

    def test_runner_initialization_invalid_name(self): # тест для исключения при неверном имени
        with self.assertRaises(TypeError, msg="Имя может быть только строкой, передано int"):
            Runner(123)

    def test_runner_initialization_invalid_speed(self): # тест для исключения при неверной скорости
        with self.assertRaises(ValueError, msg="Скорость не может быть отрицательной, сейчас -2"):
            Runner("Bob", -2)

    def test_runner_run_valid(self):  # тест для метода run
        runner = Runner("Charlie", 5)
        runner.run()
        self.assertEqual(runner.distance, 10)
        runner.run()
        self.assertEqual(runner.distance, 20)

    def test_runner_walk_valid(self): # тест для метода walk
        runner = Runner("David", 3)
        runner.walk()
        self.assertEqual(runner.distance, 3)
        runner.walk()
        self.assertEqual(runner.distance, 6)

    def test_runner_str(self): # тест для метода __str__
        runner = Runner("Eve")
        self.assertEqual(str(runner), "Eve")

    def test_runner_repr(self): # тест для метода __repr__
        runner = Runner("Frank")
        self.assertEqual(repr(runner), "Frank")

    def test_runner_eq_with_string(self): # тест для метода __eq__ при сравнении с строкой
        runner = Runner("Grace")
        self.assertEqual(runner, "Grace")
        self.assertNotEqual(runner, "NotGrace")

    def test_runner_eq_with_runner(self):  # тест для метода __eq__ при сравнении с другим Runner
        runner1 = Runner("Harry")
        runner2 = Runner("Harry")
        runner3 = Runner("Ivy")
        runner4 = Runner('Vasya')
        self.assertEqual(runner1, runner2)
        self.assertNotEqual(runner1, runner3)
        self.assertNotEqual(runner1, runner4)


# Класс TournamentTest: тесты для класса Tournament
class TournamentTest(unittest.TestCase):
    def test_tournament_start_single_runner(self): # тест для турнира с одним участником
        runner = Runner("John", 10)
        tournament = Tournament(50, runner)
        finishers = tournament.start()
        self.assertEqual(len(finishers), 1)
        self.assertEqual(finishers[1], runner)

    def test_tournament_start_multiple_runners(self): # тест для турнира с несколькими участниками
        runner1 = Runner("Kate", 5)
        runner2 = Runner("Liam", 10)
        tournament = Tournament(100, runner1, runner2)
        finishers = tournament.start()
        self.assertEqual(len(finishers), 2)
        self.assertEqual(finishers[1], runner2)
        self.assertEqual(finishers[2], runner1)

    def test_tournament_start_no_runners(self): # тест если турнир без участников
        tournament = Tournament(100)
        finishers = tournament.start()
        self.assertEqual(len(finishers), 0)

    def test_tournament_with_zero_distance(self): # тест для турнира с нулевой дистанцией
        runner1 = Runner("Mia", 1)
        tournament = Tournament(0, runner1)
        finishers = tournament.start()
        self.assertEqual(len(finishers), 1)
        self.assertEqual(finishers[1], runner1)


if __name__ == '__main__':
    RunnerTest.class_method()
    unittest.main()