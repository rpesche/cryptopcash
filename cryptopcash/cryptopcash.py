from cryptopcash.market.CryptoCompare import CryptoCompare

from cryptopcash.model.Wallet import Wallet, Holding
from cryptopcash.model.Market import Market
from cryptopcash.model.Config import Config

from cryptopcash.ui.Main import Main

from cryptopcash.storage.LocalStorage import LocalStorage


class CryptopCash(object):

    instance = None

    def __init__(self):
        self.wallet = Wallet()
        self.market = Market()
        self.config = Config()

        # get Holdings from data file
        local_storage = LocalStorage()
        holdings = local_storage.load_holdings()
        for holding in holdings:
            self.wallet.add_holding(holding)

        c = CryptoCompare()
        # Update coin information
        for holding in holdings:
            symbol = holding.coin.symbol
            holding.coin = c.get_coin_info(symbol)

        # load config file
        self.config.load()

        # Get price
        coins = [holding.coin for holding in holdings]
        if coins:
            for price in c.get_coins_prices(coins, self.config.currency):
                self.market.add_currency(price)

    def start_cryptopcash(self):
        self.main_ui = Main(self.wallet, self.market, self.config)
        self.main_ui.run()

    @staticmethod
    def get_instance():
        if not CryptopCash.instance:
            CryptopCash.instance = CryptopCash()
        return CryptopCash.instance

    def add_holding(self, coin, quantity):
        holding = Holding(coin, quantity)
        self.wallet.add_holding(holding)

        local_storage = LocalStorage()
        local_storage.save_holdings(self.wallet.holdings)
        self.main_ui.refresh()

    def get_coin_info(self, symbol):
        c = CryptoCompare()
        return c.get_coin_info(symbol)


def main():
    cryptopcash = CryptopCash.get_instance()
    cryptopcash.start_cryptopcash()


if __name__ == '__main__':
    main()
