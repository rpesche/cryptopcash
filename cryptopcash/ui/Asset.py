import urwid

from cryptopcash.ui.Value import Value


class Asset(urwid.Columns):

    def __init__(self, holding, market):

        price = market.currencies[holding.currency]

        unit = holding.unit
        currency_column = Value(holding.currency, unit)
        price_column = Value(price.price, unit)
        holding_column = Value(holding.holding, unit)
        value_column = Value(holding.holding * price.price, unit)

        high_column = Value(price.high, unit)
        low_column = Value(price.low, unit)

        super().__init__([currency_column,
                          price_column,
                          holding_column,
                          value_column,
                          high_column,
                          low_column])
