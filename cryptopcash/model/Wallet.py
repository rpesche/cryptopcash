

class Wallet(object):

    def __init__(self):
        self.holdings = []

    def add_holding(self, holding):
        coin = holding.coin
        new_quantity = holding.holding
        existing_holding = [holding for holding in self.holdings
                            if holding.coin == coin]
        if existing_holding:
            existing_holding[0].holding += new_quantity
        else:
            holding = Holding(coin, new_quantity)
            self.holdings.append(holding)

    def total_holding_value(self, market):
        total = 0.0
        for holding in self.holdings:
            holding_value = holding.get_holding_value(market)
            total += holding_value
        return total


class Holding(object):

    def __init__(self, coin, holding):
        self.coin = coin
        self.holding = holding

    def get_holding_value(self, market):
        currency_price = market.get_currency_price(self.coin.symbol)
        return float(self.holding) * float(currency_price.price)
