# Filename      :       001_singleton_allocator.py
# Created By    :       Suyog Shimpi
# Created Date  :       23/05/22
import random


class Database(object):
    """Database initializer"""
    _instance = None

    def __init__(self):
        _id = random.randint(1, 101)
        print(f'ID: {_id}')

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls) \
                .__new__(cls, *args, **kwargs)
        return cls._instance


if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2)
