from cryptopcash.market.CryptoCompare import CryptoCompare

from cryptopcash.model.Wallet import Wallet
from cryptopcash.model.Market import Market
from cryptopcash.model.Config import Config

from cryptopcash.ui.Main import Main

from cryptopcash.storage.LocalStorage import LocalStorage


def main():
    wallet = Wallet()
    market = Market()

    # get Holdings from data file
    local_storage = LocalStorage()
    holdings = local_storage.get_holdings()
    for holding in holdings:
        wallet.add_holding(holding)

    c = CryptoCompare()
    # Update coin information
    for holding in holdings:
        symbol = holding.coin.symbol
        holding.coin = c.get_coin_info(symbol)

    # load config file
    config = Config()
    config.load()

    # Get price
    coins = [holding.coin for holding in holdings]
    for price in c.get_coins_prices(coins, config.currency):
        market.add_currency(price)

    main_ui = Main(wallet, market, config)
    main_ui.run()
