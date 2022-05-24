# Filename      :       001_prototype.py
# Created By    :       Suyog Shimpi
# Created Date  :       23/05/22
from copy import deepcopy


class Address(object):
    """Address"""

    def __init__(self, street: str, suite: str, city: str):
        self.street = street
        self.suite = suite
        self.city = city

    def __str__(self) -> str:
        return f'{self.street}, Suite #{self.suite}, {self.city}'


class Employee(object):
    """Employee details"""

    def __init__(self, name: str, address: Address):
        self.name = name
        self.address = address

    def __str__(self) -> str:
        return f'{self.name} works at {self.address}'


if __name__ == '__main__':
    abc = Employee('ABC', Address('ABC Street', 'LONDON', 'UK'))
    print(abc)
    _def = deepcopy(abc)
    _def.name = 'DEF'
    _def.address.street = 'DEF Street'
    print()
    print(abc)
    print(_def)
