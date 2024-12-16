import unittest
import functools


def skip_if_frozen(test_method):
    @functools.wraps(test_method)
    def wrapper(self):
        if getattr(self, 'is_frozen', False):
            return test_method(self)
        else:
            raise unittest.SkipTest('Тесты в этом кейсе заморожены')

    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_run(self):
        self.assertTrue(True)

    @skip_if_frozen
    def test_walk(self):
        self.assertTrue(True)

    @skip_if_frozen
    def test_challenge(self):
        self.assertTrue(True)

    @classmethod
    def class_method(cls):
        print('this class method should be executed always')


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @skip_if_frozen
    def test_first_tournament(self):
        self.assertTrue(True)

    @skip_if_frozen
    def test_second_tournament(self):
        self.assertTrue(True)

    @skip_if_frozen
    def test_third_tournament(self):
        self.assertTrue(True)

    @classmethod
    def class_method(cls):
        print('this class method should be executed always')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(RunnerTest))
    suite.addTest(unittest.makeSuite(TournamentTest))

    runner = unittest.TextTestRunner()
    runner.run(suite)