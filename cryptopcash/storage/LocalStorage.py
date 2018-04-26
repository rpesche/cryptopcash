import os
import xdg
import json
import logging
from configparser import ConfigParser

from cryptopcash.model.Wallet import Holding
from cryptopcash.model.Market import CryptoCurrency


PREFIX_DIRECTORY_NAME = 'cryptopcash'
CONFIG_FILENAME = "config.ini"
WALLET_FILENAME = "wallet.json"


class LocalStorage(object):

    def get_locale_config_filename(self):
        return os.path.join(xdg.XDG_CONFIG_HOME,
                            PREFIX_DIRECTORY_NAME,
                            CONFIG_FILENAME)

    def get_locale_data_filename(self):
        return os.path.join(xdg.XDG_DATA_HOME,
                            PREFIX_DIRECTORY_NAME,
                            WALLET_FILENAME)

    def load_holdings(self):
        wallet_filename = self.get_locale_data_filename()

        if not os.path.exists(wallet_filename):
            return []

        try:
            with open(wallet_filename, 'r') as fd:
                holding_data = json.load(fd)
        except (FileNotFoundError, ValueError):
            logging.error("date file {} not readable".format(wallet_filename))
            return []

        holdings = []
        for currency, holding in holding_data.items():
            coin = CryptoCurrency("", currency)
            holding = Holding(coin, float(holding))
            holdings.append(holding)

        return holdings

    def save_holdings(self, holdings):
        wallet_filename = self.get_locale_data_filename()

        if not os.path.exists(wallet_filename):
            return []

        json_holdings = {held.coin.symbol: held.holding for held in holdings}

        try:
            with open(wallet_filename, 'w') as fd:
                json.dump(json_holdings, fd)
        except (FileNotFoundError, ValueError):
            logging.error("date file {} not readable".format(wallet_filename))
            return []

    def get_config(self):
        config_filename = self.get_locale_config_filename()

        parser = ConfigParser()
        parser.read(config_filename)
        return parser
