# Filename      :       001_chat_room.py
# Created By    :       Suyog Shimpi
# Created Date  :       26/05/22


class Person:  # noqa
    def __init__(self, name: str) -> None:
        self.name = name
        self.chat_log = []
        self.room = None

    def say(self, message: str) -> None:  # noqa
        self.room.broadcast(self.name, message)

    def receive(self, sender, message) -> None:  # noqa
        s = f'{sender}: {message}'
        print(f'[{self.name}`s chat session] {s}')
        self.chat_log.append(s)

    def private_message(self, who, message) -> None:  # noqa
        self.room.message(self.name, who, message)


class ChatRoom:  # noqa
    def __init__(self):
        self.people = []

    def broadcast(self, source, message) -> None:  # noqa
        for p in self.people:
            if p.name != source:
                p.receive(source, message)

    def join(self, person: Person) -> None:  # noqa
        join_msg = f'{person.name} joins the chat'
        self.broadcast('room', join_msg)
        person.room = self
        self.people.append(person)

    def message(self, source, destination, message) -> None:  # noqa
        for p in self.people:
            if p.name == destination:
                p.receive(source, message)


if __name__ == '__main__':
    _room = ChatRoom()
    john = Person('john')
    jane = Person('jane')
    _room.join(john)
    _room.join(jane)

    john.say('Hi, Room.')
    jane.say('Hey, Jonn.')

    simon = Person('Simon')
    _room.join(simon)
    simon.say('Hello everyone...')

    jane.private_message('Simon', 'Glad you could join us.')
