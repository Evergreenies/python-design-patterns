# Filename      :       003_singleton_metaclass.py
# Created By    :       Suyog Shimpi
# Created Date  :       23/05/22

class Singleton(type):
    """Singleton Metaclass"""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls) \
                .__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    """Database connector"""

    def __init__(self):
        print('Initialising connection...')


if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2)
