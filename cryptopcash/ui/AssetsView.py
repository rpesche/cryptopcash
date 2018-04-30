import urwid


class AssetsView(urwid.Pile):

    def __init__(self, assets):
        contents = [('fixed', 1, urwid.Filler(asset)) for asset in assets]
        self.content_view = urwid.Pile(contents)

        super().__init__(contents)

    def refresh_assets(self, new_assets):
        new_contents = [(urwid.Filler(asset), ('given', 1)) for asset in new_assets]
        self.contents = new_contents
