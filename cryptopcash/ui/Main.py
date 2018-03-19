import urwid

from cryptopcash.ui.Asset import Asset
from cryptopcash.ui.Title import Title
from cryptopcash.ui.Header import Header
from cryptopcash.ui.TotalHolding import TotalHolding


class Main(object):

    def __init__(self, wallet, market):

        def show_or_exit(key):
            if key in ('q', 'Q'):
                raise urwid.ExitMainLoop()

        palette = self.get_palette()
        main_ui = self.create_ui(wallet, market)
        self.loop = urwid.MainLoop(main_ui, palette,
                                   unhandled_input=show_or_exit)

    def create_ui(self, wallet, market):

        title = Title()
        header = Header()
        assets = [Asset(holding, market) for holding in wallet.holdings]
        total = TotalHolding(wallet, market)

        listwalker = urwid.SimpleListWalker([header, *assets])
        list_box = urwid.ListBox(listwalker)

        frame = urwid.Frame(list_box, header=title, footer=total)

        return urwid.AttrMap(frame, 'default')

    def get_palette(self):
        return [('default', 'yellow', 'black'),
                ('highlighted', 'black', 'yellow')]

    def run(self):
        self.loop.run()
