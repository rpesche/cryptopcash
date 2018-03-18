

class Market(object):

    def __init__(self):
        self.currencies = {}

    def add_currency(self, currency):
        self.currencies[currency.name] = currency


class CryptoCurrency(object):

    def __init__(self, name, unit, price, high=0.0, low=0.0):
        self.name = name
        self.unit = unit

        self.price = price
        self.low = low
        self.high = high
