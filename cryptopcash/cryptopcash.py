from cryptopcash.model.Wallet import Wallet
from cryptopcash.model.Market import Market, CryptoCurrency, CurrencyPrice

from cryptopcash.ui.Main import Main

from cryptopcash.storage.LocalStorage import LocalStorage


def main():
    wallet = Wallet()
    market = Market()

    btc = CryptoCurrency("Bitcoin", "BTC")
    ltc = CryptoCurrency("Litecoin", "LTC")
    eth = CryptoCurrency("Ethereum", "ETH")
    iota = CryptoCurrency("IOTA", "IOT")

    btc_price = CurrencyPrice(btc, 7800, 8000, 7500)
    ltc_price = CurrencyPrice(ltc, 580, 750, 550)
    eth_price = CurrencyPrice(eth, 890, 900, 885)
    iota_price = CurrencyPrice(iota, 890, 900, 885)

    market.add_currency(btc_price)
    market.add_currency(ltc_price)
    market.add_currency(eth_price)
    market.add_currency(iota_price)

    local_storage = LocalStorage()
    holdings = local_storage.get_holdings()
    for holding in holdings:
        wallet.add_holding(holding)

    main_ui = Main(wallet, market)
    main_ui.run()


main()
