# Filename      :       002_property_events.py
# Created By    :       Suyog Shimpi
# Created Date  :       26/05/22

class Event(list):  # noqa
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class PropertyObservable:  # noqa
    def __init__(self):
        self.property_changed = Event()


class Person(PropertyObservable):  # noqa
    def __init__(self, age: int = 0):
        super(Person, self).__init__()
        self._age = age

    @property
    def can_vote(self):  # noqa
        return self._age >= 18

    @property
    def age(self) -> int:  # noqa
        return self._age

    @age.setter
    def age(self, value: int) -> None:  # noqa
        if self._age == value:
            return
        old_can_vote = self.can_vote

        self._age = value
        self.property_changed('age', value)

        if old_can_vote != self.can_vote:
            self.property_changed('can_vote', self.can_vote)


class TrafficAuthority:  # noqa
    def __init__(self, person: Person):
        self.person = person
        self.person.property_changed.append(self.person_chaged)

    def person_chaged(self, name: str, value: int) -> None:  # noqa
        if name == 'age':
            if value < 16:
                print('You cannot drive yet.')
            else:
                print('Okay, You can drive now...')
                self.person.property_changed.remove(
                    self.person_chaged
                )


if __name__ == '__main__':
    _person = Person()
    ta = TrafficAuthority(_person)
    for _age in range(14, 20):
        print(f'Setting age to {_age}')
        _person.age = _age


    def person_changed(name: str, value: int) -> None:  # noqa
        if name == 'can_vote':
            print(f'Voting ability changed to {value}')


    print()
    print('Voting observer')
    _person2 = Person()
    _person2.property_changed.append(
        person_changed
    )
    for _age in range(16, 21):
        _person2.age = _age
        print(f'Changing age to {_age}')
