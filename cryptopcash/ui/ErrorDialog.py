import urwid

from cryptopcash.ui.Popup import Popup

class DialogException(Exception):
    def __init__(self, text):
        self.text = text


class ErrorDialog(Popup):

    def __init__(self, loop, exception, *args, **kwargs):
        self.text = exception.text

        Popup.__init__(self, loop, args, kwargs)

    def get_ui(self, *args, **kwargs):

        exit_button = urwid.Button('Done')
        error_text = urwid.Text(self.text)

        text_column = urwid.Columns([error_text])
        button_column = urwid.Columns([exit_button])
        pile = urwid.Pile([text_column, button_column])

        self.widget = urwid.Filler(pile, 'top')

        urwid.connect_signal(exit_button, 'click', self.exit)

        return self.widget
