# Filename      :       001_strategy_example.py
# Created By    :       Suyog Shimpi
# Created Date  :       26/05/22
from abc import ABC
from enum import Enum, auto


class ListStrategy(ABC):  # noqa
    def start(self, buffer):  # noqa
        pass

    def end(self, buffer):  # noqa
        pass

    def add_list_item(self, buffer, item):  # noqa
        pass


class MarkdownListStrategy(ListStrategy):  # noqa
    def add_list_item(self, buffer, item):  # noqa
        buffer.append(f' * {item}\n')


class HTMLListStrategy(ListStrategy):  # noqa

    def start(self, buffer):  # noqa
        buffer.append('<ul>\n')

    def end(self, buffer):  # noqa
        buffer.append('</ul>\n')

    def add_list_item(self, buffer, item):  # noqa
        buffer.append(f'  <li>{item}</li>\n')


class OutputFormat(Enum):  # noqa
    MARKDOWN = auto()  # noqa
    HTML = auto()  # noqa


class TextProcessor:  # noqa
    def __init__(self, list_strategy=HTMLListStrategy()):
        self.list_strategy = list_strategy
        self.buffer = []

    def append_list(self, items: list):  # noqa
        ls = self.list_strategy
        ls.start(self.buffer)

        for item in items:
            ls.add_list_item(self.buffer, item)
        ls.end(self.buffer)

    def set_output_format(self, format):  # noqa
        if format == OutputFormat.MARKDOWN:
            self.list_strategy = MarkdownListStrategy()
        elif format == OutputFormat.HTML:
            self.list_strategy = HTMLListStrategy()

    def clear(self):  # noqa
        self.buffer.clear()

    def __str__(self):
        return ''.join(self.buffer)


if __name__ == '__main__':
    _items = ['foo', 'bar', 'baz']

    _tp = TextProcessor()
    _tp.set_output_format(OutputFormat.MARKDOWN)
    _tp.append_list(_items)
    print(_tp)

    _tp.set_output_format(OutputFormat.HTML)
    _tp.clear()
    _tp.append_list(_items)
    print(_tp)
