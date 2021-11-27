from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def do_stuff(self):
        pass


class ConcreteProductA(Product):
    def do_stuff(self):
        print(f'Me ConcreteProductA class doing stuff!')


class ConcreteProductB(Product):
    def do_stuff(self):
        print(f'Me ConcreteProductB class doing stuff!')


class Creator(ABC):

    def some_operation(self):
        product = self.create_product()
        product.do_stuff()

    @abstractmethod
    def create_product(self):
        pass


class ConcreteCreatorA(Creator):

    def create_product(self):
        return ConcreteProductA()


class ConcreteCreatorB(Creator):

    def create_product(self):
        return ConcreteProductB()


if __name__ == '__main__':
    concrete_creator_a = ConcreteCreatorA()
    concrete_creator_a.some_operation()

    concrete_creator_b = ConcreteCreatorB()
    concrete_creator_b.some_operation()
