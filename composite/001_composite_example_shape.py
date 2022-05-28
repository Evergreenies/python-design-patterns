# Filename      :       001_composite_example_shape.py
# Created By    :       Suyog Shimpi
# Created Date  :       25/05/22

class GraphicObject:  # noqa
    def __init__(self, color=None):
        self.color = color
        self.children = []
        self._name = 'Group'

    @property
    def name(self) -> str:  # noqa
        return self._name

    def _print(self, items: list, depth: int) -> None:
        items.append('*' * depth)
        if self.color:
            items.append(self.color)
        items.append(f'{self.name}\n')
        for child in self.children:
            child._print(items, depth + 1)  # noqa

    def __str__(self):
        items = []
        self._print(items, 0)
        return ''.join(items)


class Circle(GraphicObject):  # noqa
    @property
    def name(self) -> str:  # noqa
        return 'Circle'


class Square(GraphicObject):  # noqa
    @property
    def name(self) -> str:  # noqa
        return 'Square'


if __name__ == '__main__':
    drawing = GraphicObject()
    drawing._name = 'My drawing'
    drawing.children.append(Square('Red'))
    drawing.children.append(Circle('Yellow'))

    group = GraphicObject()
    group.children.append(Circle('Blue'))
    group.children.append(Square('Blue'))
    drawing.children.append(group)

    print(drawing)
