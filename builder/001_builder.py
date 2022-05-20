# Filename      :       001_builder.py
# Created By    :       Suyog Shimpi
# Created Date  :       20/05/22
from __future__ import annotations
from typing import Any


class HTMLElement:
    """Preparing HTML Elements"""
    indent_size = 4

    def __init__(self, name: Any = '', text: str = ''):
        self.text = text
        self.name = name
        self.elements = []

    def __str(self, indent: int = 0):
        lines = []
        indentations = ' ' * (indent * self.indent_size)
        lines.append(f'{indentations}<{self.name}>')

        if self.text:
            nested_indentations = ' ' * ((indent + 1) * self.indent_size)
            lines.append(f'{nested_indentations}{self.text}')

        for element in self.elements:
            lines.append(element.__str(indent + 1))

        lines.append(f'{indentations}</{self.name}>')
        return '\n'.join(lines)

    @staticmethod
    def create(name: str) -> HTMLBuilder:
        """Creating builder object"""
        return HTMLBuilder(name)

    def __str__(self):
        return self.__str(0)


class HTMLBuilder:
    """Building elements"""

    def __init__(self, root_name: str):
        self.root_name = root_name
        self.__root = HTMLElement(root_name)

    def add_child(self, child_name: str, child_text: str) -> None:
        """
        Adding child

        :param child_name:
        :type child_name:
        :param child_text:
        :type child_text:
        :return:
        :rtype:
        """
        self.__root.elements.append(
            HTMLElement(child_name, child_text)
        )

    def add_child_fluent(self, child_name: str, child_text: str) -> HTMLBuilder:
        """
        Adding child elements

        :param child_name:
        :type child_name:
        :param child_text:
        :type child_text:
        :return:
        :rtype:
        """
        self.__root.elements.append(
            HTMLElement(child_name, child_text)
        )
        return self

    def __str__(self):
        return str(self.__root)


if __name__ == '__main__':
    builder = HTMLElement.create('ul')
    builder.add_child('li', 'hello')
    builder.add_child('li', 'world')

    # Adding child elements fluently
    builder.add_child_fluent('li', 'of').add_child_fluent('li', 'Python 3.9')

    print('Ordinary Builder')
    print(builder)
