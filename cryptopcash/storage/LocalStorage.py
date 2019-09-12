import os
import xdg
import json
import logging
from configparser import ConfigParser
from pathlib import Path
import shutil

from cryptopcash.model.Wallet import Holding
from cryptopcash.model.Market import CryptoCurrency
from cryptopcash import util


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

        json_holdings = {held.coin.symbol: held.holding for held in holdings}

        try:
            with open(wallet_filename, 'w+') as fd:
                json.dump(json_holdings, fd)
        except (FileNotFoundError, ValueError):
            logging.error("date file {} not readable".format(wallet_filename))
            return []

    def get_config(self):
        config_filename = self.get_locale_config_filename()
        if not Path(config_filename).exists():
            self.copy_default_config(config_filename)

        parser = ConfigParser()
        parser.read(config_filename)
        return parser

    def get_default_config_filename(self):
        return util.get_resource_path() / 'config' / CONFIG_FILENAME

    def copy_default_config(self, config_filename):
        default_config_filename = self.get_default_config_filename()

        config_path = Path(config_filename).parents[0]
        if not config_path.exists():
            config_path.mkdir()

        shutil.copyfile(default_config_filename, config_filename)
