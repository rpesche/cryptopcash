

class Wallet(object):

    def __init__(self):
        self.holdings = []

    def add_holding(self, holding):
        self.holdings.append(holding)


class Holding(object):

    def __init__(self, currency, holding, unit):
        self.currency = currency
        self.holding = holding
        self.unit = unit
