import urwid


class Popup(urwid.Overlay):

    def __init__(self, loop, *args, **kwargs):
        self.old_widget = None
        self.loop = loop

        widget = self.get_ui(args, kwargs)

        super().__init__(widget,
                         loop.widget,
                         align=("relative", 50),
                         valign=("relative", 25),
                         width=("relative", 20),
                         height=6)

    def get_ui(self, *args, **kwargs):
        raise NotImplemented

    def start(self):
        self.old_widget = self.loop.widget
        self.loop.widget = self

    def exit(self, *args, **kwargs):
        self.loop.widget = self.old_widget
