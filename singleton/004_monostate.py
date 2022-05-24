# Filename      :       004_monostate.py
# Created By    :       Suyog Shimpi
# Created Date  :       23/05/22

class CEO:  # noqa
    __shared_state = {
        'name': 'ABC',
        'age': 55
    }

    def __init__(self):
        self.__dict__ = self.__shared_state

    def __str__(self):
        return f'{self.name} is {self.age} years old.'  # noqa


class Monostate:
    """Monostate design pattern"""
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj


class CFO(Monostate):
    def __init__(self):
        self.name = ''
        self.money_managed = 0

    def __str__(self):
        return f'{self.name} manages ${self.money_managed}'


if __name__ == '__main__':
    # ceo1 = CEO()
    # print(ceo1)
    #
    # ceo2 = CEO()
    # ceo2.age = 77
    # print(ceo1)
    # print(ceo2)

    cfo1 = CFO()
    cfo1.name = 'ABC'
    cfo1.money_managed = 1
    print(cfo1)

    cfo2 = CFO()
    cfo2.name = 'DEF'
    cfo2.money_managed = 10
    print(cfo1)
    print(cfo2)
