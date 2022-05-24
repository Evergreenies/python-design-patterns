# Filename      :       001_bridge.py
# Created By    :       Suyog Shimpi
# Created Date  :       23/05/22
from abc import ABC


class Renderer(ABC):  # noqa
    def render_circle(self, radius):  # noqa
        pass


class VectorRendere(Renderer):  # noqa
    def render_circle(self, radius):  # noqa
        print(f'Drawing a circle of radius {radius}')


class RasterRendere(Renderer):  # noqa
    def render_circle(self, radius):  # noqa
        print(f'Drawing pixels for a circle of radius {radius}')


class Shape:  # noqa
    def __init__(self, renderer):
        self.renderer = renderer

    def draw(self):  # noqa
        pass

    def resize(self, factor):  # noqa
        pass


class Circle(Shape):  # noqa
    def __init__(self, renderer, radius):
        super(Circle, self).__init__(renderer)
        self.radius = radius

    def draw(self):  # noqa
        self.renderer.render_circle(self.radius)

    def resize(self, factor):  # noqa
        self.radius *= factor


if __name__ == '__main__':
    raster = RasterRendere()
    vector = VectorRendere()
    circle = Circle(vector, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()
