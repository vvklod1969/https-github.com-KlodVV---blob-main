import unittest
from runner_test import RunnerTest
from tournament_test import TournamentTest

all_tests = unittest.TestSuite()

all_tests.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
all_tests.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)

runner.run(all_tests)