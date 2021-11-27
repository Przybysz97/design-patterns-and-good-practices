from abc import ABC, abstractmethod
from typing import List, Optional


class Component(ABC):
    @abstractmethod
    def execute(self):
        pass


class Leaf(Component):
    def __init__(self, name):
        self._name = name

    def execute(self):
        print(f'{self._name} - Leaf operation')


class Composite(Component):

    def __init__(self):
        self._children: Optional[List[Component]] = []

    def add(self, component: Component):
        self._children.append(component)

    def remove(self, component: Component):
        self._children.remove(component)

    def get_children(self):
        return self._children

    def execute(self):
        for child in self._children:
            child.execute()


if __name__ == '__main__':
    composite = Composite()
    composite.add(Leaf('1'))
    composite.add(Leaf('2'))
    composite.add(Leaf('3'))

    parent_composite = Composite()
    parent_composite.add(Leaf('4'))
    parent_composite.add(composite)
    parent_composite.execute()
