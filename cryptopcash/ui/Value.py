import urwid
from babel import numbers


class Value(urwid.Text):

    def __init__(self, value, currency):
        rendered_text = self.render_value(value, currency)
        super().__init__(rendered_text, 'right')

    def render_value(self, value, currency):
        return numbers.format_currency(value, currency)
