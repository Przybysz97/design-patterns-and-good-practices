from abc import ABC, abstractmethod


class ProductActionsInterface(ABC):

    @abstractmethod
    def show_reviews(self):
        pass

    @abstractmethod
    def find_in_outlet(self):
        pass

    @abstractmethod
    def try_for_seven_days(self):
        pass


class ComputerActionsUI(ProductActionsInterface):
    def try_for_seven_days(self):  # cannot be implemented!
        pass

    def find_in_outlet(self):
        pass

    def show_reviews(self):
        pass


class SoftwareActionsUI(ProductActionsInterface):
    def try_for_seven_days(self):
        pass

    def find_in_outlet(self):  # cannot be implemented!
        pass

    def show_reviews(self):
        pass
