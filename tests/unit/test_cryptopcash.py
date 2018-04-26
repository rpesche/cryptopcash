"""
test about CryptopCash class
"""
import pytest
from mock import MagicMock

from cryptopcash.cryptopcash import CryptopCash
from cryptopcash.model.Market import CryptoCurrency


def test_instance():
    assert not CryptopCash.instance
    first_instance = CryptopCash.get_instance()

    next_instance = CryptopCash.get_instance()
    assert next_instance == first_instance


@pytest.mark.parametrize('data_file', [
    {'LTC': 40, 'BTC': 50}],
    indirect=True)
def test_load_holding(data_file):
    cryptopcash = CryptopCash.get_instance()

    holdings = cryptopcash.wallet.holdings

    assert holdings
    assert len(holdings) == 2
    assert holdings[0].coin.symbol == 'LTC'
    assert holdings[0].holding == 40.0
    assert holdings[1].coin.symbol == 'BTC'
    assert holdings[1].holding == 50.0


def test_add_holding():
    cryptopcash = CryptopCash.get_instance()
    cryptopcash.main_ui = MagicMock()

    coin = CryptoCurrency('Bitcoin', 'BTC')
    cryptopcash.add_holding(coin, 50)

    holdings = cryptopcash.wallet.holdings
    assert holdings
    assert len(holdings) == 1
