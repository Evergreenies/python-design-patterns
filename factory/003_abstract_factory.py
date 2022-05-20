# Filename      :       003_abstract_factory.py
# Created By    :       Suyog Shimpi
# Created Date  :       20/05/22
from abc import ABC
from enum import Enum, auto


class HotDrink(ABC):
    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print('Tea is delicious.')


class Coffee(HotDrink):
    def consume(self):
        print('Coffee is delicious.')


class HotDrinkFactory(ABC):
    def prepare(self, amount: int):
        pass


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount: int):
        print('Something to prepare tea...')
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount: int):
        print('Something to prepare coffee...')
        return Coffee()


def make_drink(_type):
    if _type == 'tea':
        return TeaFactory().prepare(100)
    elif _type == 'coffee':
        return CoffeeFactory().prepare(50)
    return None


class HotDrinkMachine:
    class AvailableDrink(Enum):
        COFFEE = auto()
        TEA = auto()

    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for drk in self.AvailableDrink:
                name = drk.name[0] + drk.name[1:].lower()
                factory_name = name + 'Factory'
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def make_drink(self):
        print('Available drinks: ')
        for factory in self.factories:
            print(factory[0])

        s = input(f'Please peak drink (0-{len(self.factories) - 1}): ')
        index = int(s)
        s = input('Specify amount: ')
        amount = int(s)
        return self.factories[index][1].prepare(amount)


if __name__ == '__main__':
    hdm = HotDrinkMachine()
    hdm.make_drink()
