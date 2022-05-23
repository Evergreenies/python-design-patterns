# Filename      :       006_exercise_factory.py
# Created By    :       Suyog Shimpi
# Created Date  :       21/05/22


class Person:  # noqa
    def __init__(self, _id: int, name: str):
        self.id = _id
        self.name = name


class PersonFactory:  # noqa
    _id = 0

    def create_person(self, name: str):  # noqa
        prn = Person(self._id, name)
        prn.id += 1
        self._id = prn.id
        return prn


if __name__ == '__main__':
    person = PersonFactory()
    p1 = person.create_person(name='Nayana')
    print(f'Person with Name: {p1.name} and ID: {p1.id}')
    p2 = person.create_person(name='Suyog')
    print(f'Person with Name: {p2.name} and ID: {p2.id}')
