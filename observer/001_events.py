# Filename      :       001_events.py
# Created By    :       Suyog Shimpi
# Created Date  :       26/05/22


class Event(list):  # noqa
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Person:  # noqa
    def __init__(self, name: str, address: str) -> None:
        self.name = name
        self.address = address
        self.falls_ill = Event()

    def catch_a_cold(self):  # noqa
        self.falls_ill(self.name, self.address)


def call_doctor(name: str, address: str):  # noqa
    print(f'{name} needs a doctor at {address}')


if __name__ == '__main__':
    _person = Person('ABC', 'XYZ')
    _person.falls_ill.append(call_doctor)
    _person.catch_a_cold()
