# Filename      :       003_iterator_example.py
# Created By    :       Suyog Shimpi
# Created Date  :       26/05/22
from collections.abc import Iterator, Iterable
from typing import Any


class AlphabeticalOrderIterator(Iterator):
    """
    Concrete Iterators implement various traversal algorithms. These classes
    store the current traversal position at all times.
    """
    # `_position` attribute stores the current traversal position. An iterator
    # may have a lot of other fields for storing interation state, especially
    # when it is supposed to work with particular kind of collection.
    _position = None
    _reverse = None  # This attribute indicates the traversal direction.

    def __init__(self, collection, reverse: bool = False) -> None:
        self._reverse = reverse
        self._collection = collection
        self._position = -1 if reverse else 0

    def __next__(self):
        """
        The __next__() method must return the next item in the sequence. On reaching
        the end, and in subsequent calls, it must raise StopIteration.
        :return:
        :rtype:
        """
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        return value


class WordsCollection(Iterable):
    """
    Concrete collection provide one or several methods for retrieving fresh iterator
    instances, compatible with the collection class.
    """

    def __init__(self, collection: list = None) -> None:
        if collection is None:
            collection = []
        self._collection = collection

    def __iter__(self) -> AlphabeticalOrderIterator:
        """
        The __iter__() method returns the iterator object itself, by default we return
        the iterator in ascending order.
        :return:
        :rtype:
        """
        return AlphabeticalOrderIterator(self._collection)

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:  # noqa
        return AlphabeticalOrderIterator(self._collection, True)

    def add_item(self, item: Any) -> None:  # noqa
        self._collection.append(item)


if __name__ == '__main__':
    _collection = WordsCollection()
    _collection.add_item('First')
    _collection.add_item('Second')
    _collection.add_item('Third')

    print()
    print('Strait traversal:')
    print('\n'.join(_collection))
    print()
    print('Reverse traversal:')
    print('\n'.join(_collection.get_reverse_iterator()))
