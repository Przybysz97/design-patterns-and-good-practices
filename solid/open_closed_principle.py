class EasterDiscount:
    _EASTER_DISCOUNT = '30%'

    def get_easter_discount(self):
        return f'{self._EASTER_DISCOUNT} on Easter'


class BlackFridayDiscount:
    _BLACK_FRIDAY_DISCOUNT = '50%'

    def get_black_friday_discount(self):
        return f'{self._BLACK_FRIDAY_DISCOUNT} on Black Friday'


class DiscountManager:

    def process_easter_discount(self, easter_discount: EasterDiscount):
        pass

    def process_black_friday_discount(self, black_friday_discount: BlackFridayDiscount):
        pass
