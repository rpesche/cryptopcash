import urwid

from cryptopcash.ui.Asset import Asset
from cryptopcash.ui.Title import Title
from cryptopcash.ui.Header import Header
from cryptopcash.ui.TotalHolding import TotalHolding
from cryptopcash.ui.AddHoldingDialog import AddHoldingDialog
from cryptopcash.ui.AssetsView import AssetsView


class Main(object):

    def __init__(self, wallet, market, conf):

        def show_or_exit(key):
            if key in ('q', 'Q'):
                raise urwid.ExitMainLoop()
            if key == 'a':
                dialog = AddHoldingDialog(self.loop)
                dialog.start()

        palette = self.get_palette(conf)
        main_ui = self.create_ui(wallet, market, conf)
        self.loop = urwid.MainLoop(main_ui, palette,
                                   unhandled_input=show_or_exit)

    def create_ui(self, wallet, market, conf):

        title = Title()
        header = Header()
        assets = [Asset(holding, market, conf) for holding in wallet.holdings]
        self.assets_view = AssetsView(assets)
        total = TotalHolding(wallet, market, conf)

        contents_view = urwid.LineBox(urwid.Frame(self.assets_view, header=header))
        main_view = urwid.Frame(contents_view, header=title, footer=total)

        return urwid.AttrMap(main_view, 'default')

    def get_palette(self, config):
        return [('default', config.text, 'black'),
                ('highlighted', config.banner_text, config.banner)]

    def run(self):
        self.loop.run()

    def refresh(self):
        from cryptopcash.cryptopcash import CryptopCash
        context = CryptopCash.get_instance()

        wallet = context.wallet
        market = context.market
        conf = context.config

        new_assets = [Asset(holding, market, conf) for holding in wallet.holdings]
        self.assets_view.refresh_assets(new_assets)
