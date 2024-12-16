import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

# Исправленный метод start :
# Сохраняем порядок финиша всех участников, чтобы выявить и победителя, и проигравшего.
# Возвращаем не словарь, а список финишировавших в порядке их прибытия.
    def start(self):
        finishers = []  # теперь это список
        while self.participants:
            for participant in self.participants:
                if participant.distance < self.full_distance:
                    if participant.distance + (participant.speed * 2) >= self.full_distance:
                        participant.distance = self.full_distance
                    else:
                        participant.run()
                if participant.distance >= self.full_distance:
                    finishers.append(participant)
                    self.participants.remove(participant)
        return finishers

# cоздаем класс TournamentTest наследуемый от unittest.TestCase
# и атрибут класса all_results
class TournamentTest(unittest.TestCase):
    all_results = {}

# создаем метод setUpClass, в котором создается атрибут all_results в виде пустого словаря:
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

# создаем метод setUp который создает объекты с заданными именами и скоростями
    def setUp(self):
        self.usain = Runner("Усэйн", speed=10)
        self.andrey = Runner("Андрей", speed=9)
        self.nick = Runner("Ник", speed=3)

# создаем метод tearDownClass который выводит результаты тестов в виде словаря где:
    # ключ - метод теста, а заначение - словарь с результатами забега
    @classmethod
    def tearDownClass(cls):
        print("\nРезультаты тестов:")
        for key, value in cls.all_results.items():
            print(f"{key}: Победитель: {value['winner']}, Проигравший: {value['loser']}")

# создадаем методы тестирования забегов где:
    # создаем объект Tournament с определенной дистанцией и участниками;
    # запускаем метод start и сохраняем результаты в all_results;
    # проверяем имя последнего бегуна.
    def test_race_usain_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        winner = results[0]
        last_runner = results[-1]
        self.all_results[self._testMethodName] = {"winner": winner.name, "loser": last_runner.name}
        self.assertTrue(last_runner == "Ник")

    def test_race_andrey_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        winner = results[0]
        last_runner = results[-1]
        self.all_results[self._testMethodName] = {"winner": winner.name, "loser": last_runner.name}
        self.assertTrue(last_runner == "Ник")

    def test_race_all(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()
        winner = results[0]
        last_runner = results[-1]
        self.all_results[self._testMethodName] = {"winner": winner.name, "loser": last_runner.name}
        self.assertTrue(last_runner == "Ник")



if __name__ == '__main__':
    unittest.main()
