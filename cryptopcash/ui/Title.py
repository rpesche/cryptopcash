import urwid


class Title(urwid.Columns):

    def __init__(self, pallette='default'):
        text_widget = urwid.Text(self.render_value())
        super().__init__([text_widget])

    def render_value(self):
        return "cryptocash v0.1"
