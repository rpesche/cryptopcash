import os
import pytest

from cryptopcash.storage.LocalStorage import LocalStorage


def test_get_locale_config():
    locale_storage = LocalStorage()
    local_config_filename = locale_storage.get_locale_config_filename()
    assert local_config_filename
    assert os.path.exists(local_config_filename)


def test_get_locale_data():
    locale_storage = LocalStorage()
    local_data_filename = locale_storage.get_locale_data_filename()
    assert local_data_filename
    assert os.path.exists(local_data_filename)


@pytest.mark.parametrize('data_file', [
    {'LTC': 40, 'BTC': 50}],
    indirect=True)
def test_load_holdings(data_file):
    locale_storage = LocalStorage()
    holdings = locale_storage.load_holdings()

    assert holdings
    assert len(holdings) == 2
    assert holdings[0].coin.symbol == 'LTC'
    assert holdings[0].holding == 40.0
    assert holdings[1].coin.symbol == 'BTC'
    assert holdings[1].holding == 50.0


def test_get_holdings_no_wallet():
    locale_storage = LocalStorage()
    assert not locale_storage.load_holdings()
