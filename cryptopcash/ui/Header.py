import urwid


HEADERS = [("COIN", 'left'),
           ("PRICE", 'right'),
           ("HELD", 'right'),
           ("VAL", 'right'),
           ("HIGH", 'right'),
           ("LOW", 'right')]


class Header(urwid.AttrMap):

    def __init__(self, palette='highlighted'):
        columns = [urwid.Text(txt, alignment) for txt, alignment in HEADERS]
        row = urwid.Columns(columns)
        super().__init__(row, palette)
