# Filename      :       002_vehical.py
# Created By    :       Suyog Shimpi
# Created Date  :       19/05/22
from abc import ABC, abstractmethod


class Movable(ABC):  # noqa
    @abstractmethod
    def go(self):  # noqa
        pass


class Flyable(Movable):  # noqa
    @abstractmethod
    def fly(self):  # noqa
        pass


class Car(Movable):  # noqa
    def go(self):  # noqa
        print('On road')


class Aircraft(Flyable):  # noqa
    def go(self):  # noqa
        print('On track')

    def fly(self):  # noqa
        print('Now, Flying...!')


if __name__ == '__main__':
    car = Car()
    car.go()

    aircraft = Aircraft()
    aircraft.go()
    aircraft.fly()
