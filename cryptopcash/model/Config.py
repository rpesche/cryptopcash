from cryptopcash.storage.LocalStorage import LocalStorage


class Config(object):

    def __init__(self):
        # Theme
        self.text = 'yellow'
        self.banner = 'yellow'
        self.banner_text = 'black'
        self.background = -1
        self.dec_places = 2
        self.field_length = 12

        # API
        self.currency = 'USD'
        self.cache = 10

        # Locale
        self.monetary = None

    def load(self):
        storage = LocalStorage()
        parser = storage.get_config()

        self.load_section(parser, 'theme', ['text', 'banner', 'banner_text',
                                            'background', 'dec_places',
                                            'field_length'])
        self.load_section(parser, 'api', ['currency', 'cache'])
        self.load_section(parser, 'locale', ['monetary'])

    def load_section(self, parser, section_name, attributes):
        try:
            api_config = parser[section_name]
        except KeyError:
            return

        for attribute in attributes:
            attribute_value = api_config.get(attribute, None)
            if attribute_value:
                self.__setattr__(attribute, attribute_value)
