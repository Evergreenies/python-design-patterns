# Filename      :       001_method_chain.py
# Created By    :       Suyog Shimpi
# Created Date  :       25/05/22

class Creature:  # noqa
    def __init__(self, name: str, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense

    def __str__(self) -> str:
        return f'{self.name} ({self.attack}/{self.defense})'


class CreatureModifier:  # noqa
    def __init__(self, creature: Creature):
        self.creature = creature
        self.next_modifier = None

    def add_modifier(self, modifier):  # noqa
        if self.next_modifier:
            self.next_modifier.add_modifier(modifier)
        else:
            self.next_modifier = modifier

    def handle(self):  # noqa
        if self.next_modifier:
            self.next_modifier.handle()


class NoBonusesModifier(CreatureModifier):  # noqa
    def handle(self):  # noqa
        print('No Bonuses for you.')


class DoubleAttackModifier(CreatureModifier):  # noqa
    def handle(self):  # noqa
        print(f'Doubling {self.creature.name}`s attack')
        self.creature.attack *= 2
        super(DoubleAttackModifier, self).handle()


class IncreaseDefenseModifier(CreatureModifier):  # noqa
    def handle(self):  # noqa
        if self.creature.attack <= 2:
            print(f'Increasing {self.creature.name} defense')
            self.creature.defense += 1
        super(IncreaseDefenseModifier, self).handle()


if __name__ == '__main__':
    goblin = Creature('Goblin', 1, 1)
    print(goblin)
    root = CreatureModifier(goblin)
    root.add_modifier(NoBonusesModifier(goblin))
    root.add_modifier(DoubleAttackModifier(goblin))
    root.add_modifier(IncreaseDefenseModifier(goblin))
    root.add_modifier(DoubleAttackModifier(goblin))
    root.handle()
    print(goblin)
