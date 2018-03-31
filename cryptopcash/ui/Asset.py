import urwid

from cryptopcash.ui.Value import Value


class Asset(urwid.Columns):

    def __init__(self, holding, market):

        marked_price = market.get_currency_price(holding.coin.symbol)

        currency = urwid.Text(marked_price.coin.name)
        price = Value(marked_price.price, unit)
        held = Value(holding.holding, unit)
        value = Value(holding.get_holding_value(market), unit)

        high = Value(marked_price.high, unit)
        low = Value(marked_price.low, unit)

        super().__init__([currency,
                          price,
                          held,
                          value,
                          high,
                          low])
