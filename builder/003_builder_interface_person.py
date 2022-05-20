# Filename      :       003_builder_interface_person.py
# Created By    :       Suyog Shimpi
# Created Date  :       20/05/22


class Person:
    """Person details"""

    def __init__(self):
        self.name = None
        self.position = None
        self.date_of_birth = None

    @staticmethod
    def new():  # noqa
        return PersonBuilder()

    def __str__(self):
        return f'{self.name} born on {self.date_of_birth} works as {self.position}'


class PersonBuilder:
    """Person builder interface"""

    def __init__(self):
        self.person = Person()

    def build(self):  # noqa
        return self.person


class PersonInfoBuilder(PersonBuilder):
    """Person info builder"""

    def called(self, name: str):  # noqa
        self.person.name = name
        return self


class PersonJobBuilder(PersonInfoBuilder):
    """Person job builder"""

    def works_as_a(self, position: str):  # noqa
        self.person.position = position
        return self


class PersonBirthDateBuilder(PersonJobBuilder):
    """Person date of birth builder"""

    def born(self, date_of_birth: str):  # noqa
        self.person.date_of_birth = date_of_birth
        return self


if __name__ == '__main__':
    pb = PersonBirthDateBuilder()
    me = pb \
        .called('ABC') \
        .works_as_a('TEMP') \
        .born('1/1/1998') \
        .build()
    print(me)
