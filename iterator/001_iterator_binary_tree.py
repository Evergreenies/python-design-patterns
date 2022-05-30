# Filename      :       001_iterator_binary_tree.py
# Created By    :       Suyog Shimpi
# Created Date  :       25/05/22

class Node:  # noqa
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = None

        if left:
            self.left.parent = self
        if right:
            self.right.parent = self

    def __iter__(self):
        return InOrderIterator(self)


class InOrderIterator:  # noqa
    def __init__(self, root):
        self.root = self.current = root
        self.yielded_start = False

        while self.current.left:
            self.current = self.current.left

    def __next__(self):
        if not self.yielded_start:
            self.yielded_start = True
            return self.current

        if self.current.right:
            self.current = self.current.right
            while self.current.left:
                self.current = self.current.left
            return self.current
        else:
            p = self.current.parent
            while p and self.current == p.right:
                self.current = p
                p = p.parent
            self.current = p
            if self.current:
                return self.current
            else:
                raise StopIteration


def traverse_in_order(root):  # noqa
    def traverse(current):  # noqa
        if current.left:
            for left in traverse(current.left):
                yield left
        yield current
        if current.right:
            for right in traverse(current.right):
                yield right

    for node in traverse(root):
        yield node


if __name__ == '__main__':
    _root = Node(
        1,
        Node(2),
        Node(3),
    )
    it = iter(_root)

    print([next(it).value for _ in range(3)])

    for x in _root:
        print(x.value)

    for y in traverse_in_order(_root):
        print(y.value)
