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

        # get Holdings from data file
        local_storage = LocalStorage()
        holdings = local_storage.get_holdings()
        for holding in holdings:
            self.wallet.add_holding(holding)

        c = CryptoCompare()
        # Update coin information
        for holding in holdings:
            symbol = holding.coin.symbol
            holding.coin = c.get_coin_info(symbol)

        # load config file
        self.config = Config()
        self.config.load()

        # Get price
        self.market = Market()
        coins = [holding.coin for holding in holdings]
        for price in c.get_coins_prices(coins, self.config.currency):
            self.market.add_currency(price)

    def start_cryptopcash(self):
        main_ui = Main(self.wallet, self.market, self.config)
        main_ui.run()

    @staticmethod
    def get_instance():
        if not CryptopCash.instance:
            CryptopCash.instance = CryptopCash()
        return CryptopCash.instance

    def add_holding(self, coin, quantity):
        holding = Holding(coin, quantity)
        self.wallet.add_holding(holding)

    def get_coin_info(self, coin):
        c = CryptoCompare()
        return c.get_coin_info(coin.symbol)


def main():
    cryptopcash = CryptopCash.get_instance()
    cryptopcash.start_cryptopcash()


if __name__ == '__main__':
    main()
