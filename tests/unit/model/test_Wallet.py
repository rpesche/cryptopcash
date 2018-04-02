import pytest

from cryptopcash.model.Wallet import Wallet, Holding
from cryptopcash.model.Market import CryptoCurrency


@pytest.mark.parametrize("adds, result", [
    ([],
     []),

    ([('BTC', 30)],
     [('BTC', 30)]),

    ([('BTC', 30), ('BTC', 20)],
     [('BTC', 50)]),

    ([('BTC', 30), ('LTC', 42), ('BTC', 20)],
     [('BTC', 50), ('LTC', 42)]),
])
def test_add_holding(adds, result):
    wallet = Wallet()

    for symbol, quantity in adds:
        coin = CryptoCurrency(symbol, symbol)
        holding = Holding(coin, quantity)
        wallet.add_holding(holding)

    holdings = wallet.holdings
    crypto_held = [symbol for symbol, _ in result]
    result_held = [holding.coin.symbol for holding in holdings]

    assert set(result_held) == set(crypto_held)

    for symbol, quantity in result:
        holding = [holding.holding for holding in holdings if holding.coin.symbol == symbol]
        assert holding[0] == quantity
