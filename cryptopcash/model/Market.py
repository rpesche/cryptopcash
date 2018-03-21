

class Market(object):

    def __init__(self):
        self.currencies = {}

    def add_currency(self, currency):
        self.currencies[currency.coin.symbol] = currency

    def get_currency_price(self, symbol):
        return self.currencies.get(symbol, None)


class CryptoCurrency(object):

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


class CurrencyPrice(object):

    def __init__(self, coin, price, low, high):
        self.coin = coin
        self.price = price
        self.low = low
        self.high = high
