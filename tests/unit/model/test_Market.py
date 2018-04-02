import pytest

from cryptopcash.model.Market import CryptoCurrency


@pytest.mark.parametrize("param_a, param_b, res", [
    ({'name': 'Bitcoin', 'symbol': 'BTC'}, {'name': 'err', 'symbol': 'BTC'}, True),
    ({'name': 'Bitcoin', 'symbol': 'BTC'}, {'name': 'Bitcoin', 'symbol': 'BCH'}, False),
 ])
def test_equal_coin(param_a, param_b, res):
    coin_a = CryptoCurrency(**param_a)
    coin_b = CryptoCurrency(**param_b)

    assert (coin_a == coin_b) == res
