import urwid

from cryptopcash.ui.Popup import Popup


class AddHoldingDialog(Popup):

    def get_ui(self, *args, **kwargs):
        self.symbol = urwid.Edit("Symbol :")
        self.holding = urwid.Edit("Holding :")
        exit_button = urwid.Button('Exit')
        submit_button = urwid.Button('Add')

        edit_column = urwid.Columns([self.symbol, self.holding])
        button_column = urwid.Columns([submit_button, exit_button])
        pile = urwid.Pile([edit_column, button_column])

        self.widget = urwid.Filler(pile, 'top')

        urwid.connect_signal(exit_button, 'click', self.exit)
        urwid.connect_signal(submit_button, 'click', self.add_holding)

        return self.widget

    def add_holding(self, button):
        from cryptopcash.cryptopcash import CryptopCash
        context = CryptopCash.get_instance()

        symbol = self.symbol.get_edit_text()
        coin = context.get_coin_info(symbol)
        quantity = float(self.holding.get_edit_text())

        context.add_holding(coin, quantity)
        self.exit()
