# Filename      :       001_dip.py
# Created By    :       Suyog Shimpi
# Created Date  :       19/05/22

from abc import ABC, abstractmethod
from enum import Enum
from typing import Generator


class Relationship(Enum):
    """Relationship"""
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    """A person"""

    def __init__(self, name: str):
        self.name = name


class RelationshipBrowser(ABC):
    """Abstract class to search a relations"""

    @abstractmethod
    def find_all_children_of(self, name: str) -> Generator:  # noqa
        pass


class Relationships(RelationshipBrowser):
    """Adding and finding relations"""

    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent: Person, child: Person) -> None:  # noqa
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

    def find_all_children_of(self, name: str) -> Generator:  # noqa
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


class Research:
    """Research on relations"""

    def __init__(self, browser: Relationships, parent: str):
        for p in browser.find_all_children_of(parent):
            print(f'{parent} has child name {p}')


if __name__ == '__main__':
    parent1 = Person('ABC')
    child1 = Person('XYZ')
    child2 = Person('DEF')

    relationships1 = Relationships()
    relationships1.add_parent_and_child(parent1, child1)
    relationships1.add_parent_and_child(parent1, child2)

    Research(relationships1, 'ABC')
