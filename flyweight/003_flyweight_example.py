# Filename      :       003_flyweight_example.py
# Created By    :       Suyog Shimpi
# Created Date  :       25/05/22
import json
from typing import Any, Dict


class Flyweight:
    """
    The flyweight stores a common portion of the state (also called intrinsic state)
    that belongs to multiple real business entities. The flyweight accepts the rest
    of the state (extrinsic state, unique for each entity) via its method parameters.
    """

    def __init__(self, shared_state: Any) -> None:
        self._shared_state = shared_state

    def operation(self, unique_state: Any) -> None:  # noqa
        s = json.dumps(self._shared_state)
        u = json.dumps(unique_state)
        print(f'Flyweight: Displaying shared ({s}) and unique ({u}) state.')


class FlyweightFactory:
    """
    The flyweight factory creates and manages the flyweight objects. It ensures that
    flyweight are shared correctly, When the client requests a flyweight, the factory
    either returns an existing instance or creates a new one, if it doesn't exist yet.
    """

    _fylweight = {}

    def __init__(self, initial_flyweights: list) -> None:
        for state in initial_flyweights:
            self._fylweight[self.get_key(state)] = Flyweight(state)

    def get_key(self, state: Dict) -> str:  # noqa
        """
        Returns a Flyweight's string hash for given state
        :param state:
        :type state:
        :return:
        :rtype:
        """
        return '_'.join(sorted(state))

    def get_flyweight(self, shared_state: Any) -> Flyweight:
        """
        Returns an existing Flyweight with a given state or creates a new one
        :param shared_state:
        :type shared_state:
        :return:
        :rtype:
        """
        key = self.get_key(shared_state)
        if not self._fylweight.get(key):
            print('FlyweightFactory: Can`t find a flyweight, creating new one.')
            self._fylweight[key] = Flyweight(shared_state)
        else:
            print('FlyweightFactory: Reusing existing flyweight.')
        return self._fylweight[key]

    def list_flyweights(self) -> None:  # noqa
        count = len(self._fylweight)
        print(f'FlyweightFactory: I have {count} flyweights:')
        print('\n'.join(map(str, self._fylweight.keys())))


def add_car_to_police_database(  # noqa
        factory: FlyweightFactory, plates: str, owner: str,
        brand: str, model: str, color: str
):
    print('\n\nClient: Adding a car to database.')
    flyweight = factory.get_flyweight([brand, model, color])
    flyweight.operation([plates, owner])


if __name__ == '__main__':
    _factory = FlyweightFactory([
        ["Chevrolet", "Camaro2018", "pink"],
        ["Mercedes Benz", "C300", "black"],
        ["Mercedes Benz", "C500", "red"],
        ["BMW", "M5", "red"],
        ["BMW", "X6", "white"],
    ])

    _factory.list_flyweights()

    add_car_to_police_database(_factory, "CL234IR", "James Doe", "BMW", "M5", "red")
    add_car_to_police_database(_factory, "CL234IR", "James Doe", "BMW", "X1", "red")

    print()
    _factory.list_flyweights()
