# Filename      :       004_builder_of_simple_chunk_of_code.py
# Created By    :       Suyog Shimpi
# Created Date  :       20/05/22
from __future__ import annotations

from typing import Any


class PythonClass(object):
    """Python Class"""

    indent_size = 4

    def __init__(self, variable_name: str = '', value: Any = ''):
        self.value = value
        self.variable_name = variable_name
        self.fields = []

    def __str(self, indent: int = 0) -> str:
        lines = []
        indentations = ' ' * (indent * self.indent_size)

        nested_indentations = ' ' * ((indent + 1) * self.indent_size)
        if self.value:
            lines.append(f'{nested_indentations}self.{self.variable_name} = {self.value}')
        else:
            lines.append(f'{indentations}class {self.variable_name}:')
            lines.append(f'{nested_indentations}def __init__(self):')

        for field in self.fields:
            lines.append(field.__str(indent + 1))

        return '\n'.join(lines)

    @staticmethod
    def create(name: str) -> CodeBuilder:
        """Creating CodeBuilder object"""
        return CodeBuilder(name)

    def __str__(self):
        return self.__str(0)


class CodeBuilder:
    """Building Python code"""

    def __init__(self, root_name: str):
        self.root_name = root_name
        self.__root = PythonClass(root_name)

    def add_field(self, variable_name: str, value: Any) -> CodeBuilder:
        """
        Adding fields
        :param variable_name:
        :type variable_name:
        :param value:
        :type value:
        :return:
        :rtype:
        """
        self.__root.fields.append(
            PythonClass(variable_name, value)
        )
        return self

    def __str__(self):
        return str(self.__root)


if __name__ == '__main__':
    cb = CodeBuilder('Person') \
        .add_field('name', '""') \
        .add_field('age', '0')
    print(cb)
