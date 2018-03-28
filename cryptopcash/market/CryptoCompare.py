from cryptocompy import coin as cryptocompy_coin
from cryptocompy import price as cryptocompy_price

from cryptopcash.market.Market import Market

from cryptopcash.model.Market import CryptoCurrency, CurrencyPrice


class CryptoCompare(Market):

    def get_coins_list(self):
        res = cryptocompy_coin.get_coin_list()
        for symbol, coins in res.items():
            name = coins['CoinName']
            yield CryptoCurrency(name, symbol)

    def get_coin_price(self, coin, unit):
        symbol = coin.symbol

        res = cryptocompy_price.get_current_price(symbol, unit, full=True)
        infos = res[symbol][unit]
        price, high, low = self.prices_from_res_infos(infos)

        return CurrencyPrice(coin, price, low, high)

    def get_coins_prices(self, coins, unit):
        symbols = [coin.symbol for coin in coins]
        res = cryptocompy_price.get_current_price(symbols, unit, full=True)

        for symbol, info in res.items():
            price, high, low = self.prices_from_res_infos(info[unit])
            coin = [c for c in coins if c.symbol == symbol]
            yield CurrencyPrice(coin[0], price, low, high)

    def prices_from_res_infos(self, infos):
        price = infos['PRICE']
        high = infos['HIGH24HOUR']
        low = infos['LOW24HOUR']

        return price, high, low
