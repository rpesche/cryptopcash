import urwid

from cryptopcash.ui.Asset import Asset
from cryptopcash.ui.Title import Title
from cryptopcash.ui.Header import Header
from cryptopcash.ui.TotalHolding import TotalHolding
from cryptopcash.ui.AddHoldingDialog import AddHoldingDialog


class Main(object):

    def __init__(self, wallet, market, conf):

        def show_or_exit(key):
            if key in ('q', 'Q'):
                raise urwid.ExitMainLoop()
            if key == 'a':
                dialog = AddHoldingDialog(self.loop)
                dialog.start()

        palette = self.get_palette()
        main_ui = self.create_ui(wallet, market, conf)
        self.loop = urwid.MainLoop(main_ui, palette,
                                   unhandled_input=show_or_exit)

    def create_ui(self, wallet, market, conf):

        title = Title()
        header = Header()
        assets = [Asset(holding, market, conf) for holding in wallet.holdings]
        total = TotalHolding(wallet, market, conf)

        lines = [header, *assets]
        self.listwalker = urwid.Pile([('fixed', 1, urwid.Filler(line)) for line in lines])
        list_box = urwid.LineBox(self.listwalker)

        frame = urwid.Frame(list_box, header=title, footer=total)

        return urwid.AttrMap(frame, 'default')

    def get_palette(self):
        return [('default', 'yellow', 'black'),
                ('highlighted', 'black', 'yellow')]

    def run(self):
        self.loop.run()
