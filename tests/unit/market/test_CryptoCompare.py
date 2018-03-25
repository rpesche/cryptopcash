import pytest

from cryptopcash.market.CryptoCompare import CryptoCompare
from cryptopcash.model.Market import CryptoCurrency


def test_get_coins_list():
    crypto_compare = CryptoCompare()
    coins_list = list(crypto_compare.get_coins_list())

    assert coins_list
    assert len(coins_list) == 3

    assert coins_list[0].symbol == 'BTC'
    assert coins_list[1].symbol == 'LTC'
    assert coins_list[2].symbol == 'IOT'


def test_get_price():
    crypto_compare = CryptoCompare()

    btc = CryptoCurrency('Bitcoin', 'BTC')
    price = crypto_compare.get_coin_price(btc, 'EUR')
    assert price
    assert price.coin.symbol == 'BTC'
    assert price.price == 7000.00
    assert price.low == 6800.00
    assert price.high == 7200.00


@pytest.mark.parametrize("symbols", [
    ['BTC'],
    ['BTC', 'LTC'],
    ['IOT', 'ETH'],
])
def test_get_prices(symbols):
    coins = [CryptoCurrency('Bitcoin', symbol) for symbol in symbols]

    crypto_compare = CryptoCompare()
    prices = list(crypto_compare.get_coins_prices(coins, 'EUR'))

    assert prices
    assert len(prices) == len(coins)
    for price in prices:
        assert price.coin.symbol in symbols
        assert price.price == 7000.00
        assert price.low == 6800.00
        assert price.high == 7200.00
