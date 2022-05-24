# Filename      :       002_prototype_factory.py
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


class EmployeeFactory:
    """Employee factory class to reuse the protos"""
    main_office_employee = Employee('', Address('123 EAST', '0', 'Landon'))
    aux_main_office_employee = Employee('', Address('123B EAST', '0', 'Landon'))

    @staticmethod
    def __new_employee(proto, name: str, suite: str):
        result = deepcopy(proto)
        result.name = name
        result.address.suite = suite
        return result

    @staticmethod
    def new_main_office_employee(name: str, suite: str):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.main_office_employee,
            name, suite
        )

    @staticmethod
    def new_aux_main_office_employee(name: str, suite: str):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.aux_main_office_employee,
            name, suite
        )


if __name__ == '__main__':
    john = EmployeeFactory.new_main_office_employee('John', '101')
    jane = EmployeeFactory.new_aux_main_office_employee('Jane', '500')
    print(john)
    print(jane)
