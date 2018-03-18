import urwid


HEADERS = ["COIN", "PRICE", "HELD", "VAL", "HIGH", "LOW"]


class Header(urwid.AttrMap):

    def __init__(self, palette='highlighted'):
        columns = [urwid.Text(txt) for txt in HEADERS]
        row = urwid.Columns(columns)
        super().__init__(row, palette)
