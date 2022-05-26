# Filename      :       002_event_broken_chain.py
# Created By    :       Suyog Shimpi
# Created Date  :       25/05/22
from abc import ABC
from enum import Enum


class Event(list):  # noqa
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class WhatToQuery(Enum):  # noqa
    ATTACK = 1
    DEFENSE = 2


class Query:  # noqa
    def __init__(self, creature_name, what_to_query, default_value):
        self.creature_name = creature_name
        self.what_to_query = what_to_query
        self.value = default_value


class Game:  # noqa
    def __init__(self):
        self.queries = Event()

    def perform_query(self, sender, query):  # noqa
        self.queries(sender, query)


class Creature:  # noqa
    def __init__(self, game, name, attack, defense):
        self.initial_defense = defense
        self.initial_attack = attack
        self.name = name
        self.game = game

    @property
    def attack(self):  # noqa
        q = Query(self.name, WhatToQuery.ATTACK, self.initial_attack)
        self.game.perform_query(self, q)
        return q.value

    @property
    def defense(self):  # noqa
        q = Query(self.name, WhatToQuery.DEFENSE, self.initial_defense)
        self.game.perform_query(self, q)
        return q.value

    def __str__(self):
        return f'{self.name} ({self.attack}/{self.defense})'


class CreatureModifier(ABC):  # noqa
    def __init__(self, game, creature):
        self.game = game
        self.creature = creature
        self.game.queries.append(self.handle)

    def handle(self, sender, query):  # noqa
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.game.queries.remove(self.handle)



class DoubleAttackModifier(CreatureModifier):  # noqa
    def handle(self, sender, query):  # noqa
        if sender.name == self.creature.name and \
                query.what_to_query == WhatToQuery.ATTACK:
            query.value *= 2


if __name__ == '__main__':
    _game = Game()
    goblin = Creature(_game, 'Strong Goblin', 2, 2)
    print(goblin)
    with DoubleAttackModifier(_game, goblin):
        print(goblin)
    print(goblin)
