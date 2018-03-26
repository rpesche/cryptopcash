from cryptopcash.storage.LocalStorage import LocalStorage


class Config(object):

    def __init__(self):
        self.currency = ''

    def load(self):
        storage = LocalStorage()
        parser = storage.get_config()

        self.load_api_section(parser)

    def load_api_section(self, parser):
        try:
            api_config = parser['api']
        except KeyError:
            return

        self.currency = api_config.get('currency', self.currency)
