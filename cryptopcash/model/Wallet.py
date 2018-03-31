

class Wallet(object):

    def __init__(self):
        self.holdings = []

    def add_holding(self, holding):
        self.holdings.append(holding)

    def total_holding_value(self, market):
        total = 0.0
        for holding in self.holdings:
            holding_value = holding.get_holding_value(market)
            total += holding_value
        return total


class Holding(object):

    def __init__(self, coin, holding, unit):
        self.coin = coin
        self.holding = holding
        self.unit = unit

    def get_holding_value(self, market):
        currency_price = market.get_currency_price(self.coin.symbol)
        return float(self.holding) * float(currency_price.price)
