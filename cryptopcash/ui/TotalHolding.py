import urwid


class TotalHolding(urwid.AttrMap):

    def __init__(self, wallet, market, conf, palette='highlighted'):
        holdings_string = self.total_holding_str(wallet, market, conf)
        text_widget = urwid.Text(holdings_string)
        column = urwid.Columns([text_widget])

        super().__init__(column, palette)

    def total_holding_str(self, wallet, market, conf):
        total_value = wallet.total_holding_value(market)
        return "Total Holdings: {} {}".format(total_value, "€")
