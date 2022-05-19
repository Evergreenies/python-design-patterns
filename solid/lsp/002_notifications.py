# Filename      :       002_notifications.py
# Created By    :       Suyog Shimpi
# Created Date  :       19/05/22

from abc import ABC, abstractmethod


class Notification(ABC):
    """Abstract class for notifications"""

    @abstractmethod
    def notify(self, message: str) -> None:  # noqa
        pass


class Email(Notification):
    """Email notifications"""

    def __init__(self, email: str):
        self.email = email

    def notify(self, message: str) -> None:  # noqa
        print(f'Send `{message}` to `{self.email}`')


class SMS(Notification):
    """SMS notifications"""

    def __init__(self, phone_no: int):
        self.phone_no = phone_no

    def notify(self, message: str) -> None:  # noqa
        print(f'Send `{message}` to `{self.phone_no}`')


class Contact:
    """Contact details"""

    def __init__(self, name: str, email: str, phone_no: int):
        self.phone_no = phone_no
        self.email = email
        self.name = name


class NotificationManager:
    """Notification manager"""

    def __init__(self, notification: Notification):
        self.notification = notification

    def send(self, message: str) -> None:  # noqa
        self.notification.notify(message)


def notifier(notification: Notification, message: str) -> None:
    """Responsible to send notifications"""
    _notifier = NotificationManager(notification)
    _notifier.send(message)


if __name__ == '__main__':
    contact = Contact('ABC XYZ', 'abc@test.com', 403_3339999)
    notifier(SMS(contact.phone_no), 'Hello ABC')
    notifier(Email(contact.email), 'Hi ABC')
