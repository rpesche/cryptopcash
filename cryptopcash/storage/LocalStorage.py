import os
import xdg
import json
import logging

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

    def get_holdings(self):
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
            coin = CryptoCurrency(None, currency)
            holding = Holding(coin, float(holding), "")
            holdings.append(holding)

        return holdings
