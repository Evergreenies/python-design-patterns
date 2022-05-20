# Filename      :       002_person.py
# Created By    :       Suyog Shimpi
# Created Date  :       20/05/22
from __future__ import annotations


class Person:
    """Person details"""

    def __init__(self):
        self.stree_address = None
        self.postcode = None
        self.city = None

        self.company_name = None
        self.position = None
        self.annual_income = None

    def __str__(self):
        return f'Address: {self.stree_address}, {self.postcode}, {self.city}' \
               f'\nEmployed at {self.company_name} as {self.position} earning {self.annual_income} yearly'


class PersonBuilder:  # noqa _FIXME: (BROKEN) This class violates Open-Closed Principle
    """Person builder"""

    def __init__(self, person: Person = Person()):
        self.person = person

    @property
    def works(self) -> PersonJobBuilder:  # noqa
        return PersonJobBuilder(self.person)

    @property
    def lives(self) -> PersonAddressBuilder:  # noqa
        return PersonAddressBuilder(self.person)

    def build(self) -> Person:  # noqa
        return self.person

    def __str__(self):
        return f'{self.person}'


class PersonJobBuilder(PersonBuilder):
    """Person job builder"""

    def __init__(self, person: Person):
        super(PersonJobBuilder, self).__init__(person)

    def at(self, company_name: str) -> PersonJobBuilder:  # noqa
        self.person.company_name = company_name
        return self

    def as_a(self, position: str) -> PersonJobBuilder:  # noqa
        self.person.position = position
        return self

    def earning(self, annual_income: int) -> PersonJobBuilder:  # noqa
        self.person.annual_income = annual_income
        return self


class PersonAddressBuilder(PersonBuilder):
    """Person address details builder"""

    def __init__(self, person: Person):
        super(PersonAddressBuilder, self).__init__(person)

    def at(self, street_address: str) -> PersonAddressBuilder:  # noqa
        self.person.street_address = street_address
        return self

    def with_postcode(self, postcode: int) -> PersonAddressBuilder:  # noqa
        self.person.postcode = postcode
        return self

    def in_city(self, city: str) -> PersonAddressBuilder:  # noqa
        self.person.city = city
        return self


if __name__ == '__main__':
    pb = PersonBuilder()
    _person = pb \
        .lives.at('Jungle').in_city('Malpur').with_postcode(425408) \
        .works.at('Musikaar').as_a('Senior Software Developer').earning(1250000)
    print(_person)
