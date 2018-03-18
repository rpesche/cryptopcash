import urwid


class Value(urwid.Text):

    def __init__(self, value, currency):
        rendered_text = self.render_value(value, currency)
        super().__init__(rendered_text)

    def render_value(self, value, currency):
        return "{} {}".format(value, currency)
