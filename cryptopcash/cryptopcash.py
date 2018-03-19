from cryptopcash.model.Wallet import Wallet
from cryptopcash.model.Market import Market, CryptoCurrency

from cryptopcash.ui.Main import Main

from cryptopcash.storage.LocalStorage import LocalStorage


def main():
    wallet = Wallet()
    market = Market()

    market.add_currency(CryptoCurrency("Bitcoin", "BTC", 7800, 8000, 7500))
    market.add_currency(CryptoCurrency("Litecoin", "LTC", 580, 750, 550))
    market.add_currency(CryptoCurrency("Ethereum", "ETH", 890, 900, 885))
    market.add_currency(CryptoCurrency("IOTA", "IOT", 890, 900, 885))

    local_storage = LocalStorage()
    holdings = local_storage.get_holdings()
    for holding in holdings:
        wallet.add_holding(holding)

    main_ui = Main(wallet, market)
    main_ui.run()


main()
