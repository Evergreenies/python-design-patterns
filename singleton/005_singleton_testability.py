# Filename      :       005_singleton_testability.py
# Created By    :       Suyog Shimpi
# Created Date  :       23/05/22
import unittest


class Singleton(type):
    """Singleton metaclass"""
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(Singleton, cls) \
                .__call__(*args, **kwargs)
        return cls._instance[cls]


class Database(metaclass=Singleton):
    def __init__(self):
        self.population = {}
        with open('capitals.txt', 'r') as fp:
            lines = fp.readlines()
            for index in range(0, len(lines), 2):
                self.population[lines[index].strip()] = int(lines[index + 1].strip())


class SingletonRecordFinder:
    def total_population(self, cities):
        result = 0
        for city in cities:
            result += Database().population[city]
        return result


class ConfigurableDataFinder:
    def __init__(self, db):
        self.db = db

    def total_population(self, cities):
        result = 0
        for city in cities:
            result += self.db.population[city]
        return result


class DummyDatabase:
    population = {
        'alpha': 1,
        'beta': 2,
        'gamma': 3
    }

    def get_populations(self, name):
        return self.population[name]


class SingletonTest(unittest.TestCase):
    def test_is_singleton(self):
        db1 = Database()
        db2 = Database()
        self.assertEqual(db1, db2)

    def test_singleton_total_population(self):
        rf = SingletonRecordFinder()
        names = ['Seoul', 'Maxico City']
        tp = rf.total_population(names)
        self.assertEqual(17500000 + 17400000, tp)

    ddb = DummyDatabase()

    def test_dependent_total_populations(self):
        crf = ConfigurableDataFinder(self.ddb)
        self.assertEqual(3, crf.total_population(['alpha', 'beta']))
