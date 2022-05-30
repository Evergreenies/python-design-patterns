# Filename      :       001_protection_proxy.py
# Created By    :       Suyog Shimpi
# Created Date  :       25/05/22

"""
Protection Proxy - A proxy class that controls access to the particular resource.
"""


class Driver:  # noqa
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class Car:  # noqa
    def __init__(self, driver: Driver):
        self.driver = driver

    def drive(self):  # noqa
        print(f'Car is being driven by {self.driver.name}.')


class CarProxy:  # noqa
    def __init__(self, driver: Driver):
        self.driver = driver
        self._car = Car(driver)

    def drive(self):  # noqa
        if self.driver.age >= 16:
            self._car.drive()
        else:
            print('Driver too young.')


if __name__ == '__main__':
    _driver = Driver('John', 20)
    _car = CarProxy(_driver)
    _car.drive()
