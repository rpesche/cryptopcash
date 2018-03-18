from cryptopcash.model.Wallet import Wallet, Holding
from cryptopcash.model.Market import Market, CryptoCurrency

from cryptopcash.ui.Main import Main


def main():
    wallet = Wallet()
    market = Market()

    market.add_currency(CryptoCurrency("Bitcoin", "BTC", 7800, 8000, 7500))
    market.add_currency(CryptoCurrency("Litecoin", "LTC", 580, 750, 550))
    market.add_currency(CryptoCurrency("Ethereum", "ETH", 890, 900, 885))

    wallet.add_holding(Holding("Bitcoin", 0.5, "BTC"))
    wallet.add_holding(Holding("Litecoin", 0.5, "LTC"))
    wallet.add_holding(Holding("Ethereum", 0.5, "ETH"))

    main_ui = Main(wallet, market)
    main_ui.run()


main()
