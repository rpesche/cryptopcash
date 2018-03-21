from cryptopcash.market.CryptoCompare import CryptoCompare

from cryptopcash.model.Wallet import Wallet
from cryptopcash.model.Market import Market, CryptoCurrency, CurrencyPrice

from cryptopcash.ui.Main import Main

from cryptopcash.storage.LocalStorage import LocalStorage


def main():
    wallet = Wallet()
    market = Market()

    local_storage = LocalStorage()
    holdings = local_storage.get_holdings()
    for holding in holdings:
        wallet.add_holding(holding)

    coins = [holding.coin for holding in holdings]
    c = CryptoCompare()
    crypto_compare_price = c.get_coins_prices(coins, "EUR")

    for price in crypto_compare_price:
        market.add_currency(price)

    main_ui = Main(wallet, market)
    main_ui.run()
