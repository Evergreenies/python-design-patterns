# Filename      :       001_list_backed_properties.py
# Created By    :       Suyog Shimpi
# Created Date  :       26/05/22


"""
This is nothing but the example of array-backed/list-backed properties.
"""


class Creature:  # noqa
    _strength = 0
    _agility = 1
    _intelligence = 2

    def __init__(self):
        self.stats = [10, 10, 10]

    @property
    def strength(self) -> int:  # noqa
        return self.stats[Creature._strength]

    @strength.setter
    def strength(self, value: int) -> None:
        self.stats[Creature._strength] = value

    @property
    def agility(self) -> int:  # noqa
        return self.stats[Creature._agility]

    @agility.setter
    def agility(self, value: int) -> None:
        self.stats[Creature._agility] = value

    @property
    def intelligence(self) -> int:  # noqa
        return self.stats[Creature._intelligence]

    @intelligence.setter
    def intelligence(self, value: int) -> None:
        self.stats[Creature._intelligence] = value

    @property
    def sum_of_stats(self) -> int:  # noqa
        return sum(self.stats)

    @property
    def max_stat(self) -> int:  # noqa
        return max(self.stats)

    @property
    def average_stat(self) -> float:  # noqa
        return float(sum(self.stats) / len(self.stats))


if __name__ == '__main__':
    _creature = Creature()
    print(_creature.sum_of_stats)
    print(_creature.max_stat)
    print(_creature.average_stat)
