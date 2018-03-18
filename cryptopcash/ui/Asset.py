import urwid

from cryptopcash.ui.Value import Value


class Asset(urwid.Columns):

    def __init__(self, holding, market):

        price = market.currencies[holding.currency]

        unit = holding.unit
        currency = Value(holding.currency, unit)
        price = Value(price.price, unit)
        holding = Value(holding.holding, unit)
        value = Value(holding.get_holding_value(market), unit)

        high = Value(price.high, unit)
        low = Value(price.low, unit)

        super().__init__([currency,
                          price,
                          holding,
                          value,
                          high,
                          low])
