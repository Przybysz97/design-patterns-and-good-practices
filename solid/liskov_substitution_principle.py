from abc import ABC, abstractmethod


class DeliveryBase(ABC):

    def __init__(self, product_ids, user):
        self.product_ids = product_ids
        self.user = user

    @abstractmethod
    def get_delivery_location(self):
        pass


class ComputerDelivery(DeliveryBase):

    def get_delivery_location(self):
        pass


class SoftwareDelivery(DeliveryBase):

    def get_delivery_location(self):  # cannot be implemented! It's senseless!
        pass
