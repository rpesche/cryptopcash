import pytest
from cryptocompy import coin as cryptocompy_coin
from cryptocompy import price as cryptocompy_price


PRICES = {'BTC': (8000, 9000, 7000),
          'LTC': (500, 600, 400),
          'IOT': (5, 6, 3)}


@pytest.fixture(autouse=True)
def cryptocompare_mock(monkeypatch):

    monkeypatch.setattr(cryptocompy_coin, "get_coin_list", get_coin_list)
    monkeypatch.setattr(cryptocompy_price, "get_current_price", get_price)


def get_coin_list():
    return {'BTC':
            {'Algorithm': 'SHA256',
             'CoinName': 'Bitcoin',
             'FullName': 'Bitcoin (BTC)',
             'FullyPremined': '0',
             'Id': '1182',
             'ImageUrl': '/media/19633/btc.png',
             'Name': 'BTC',
             'PreMinedValue': 'N/A',
             'ProofType': 'PoW',
             'SortOrder': '1',
             'Sponsored': False,
             'Symbol': 'BTC',
             'TotalCoinSupply': '21000000',
             'TotalCoinsFreeFloat': 'N/A',
             'Url': '/coins/btc/overview'},
            'LTC':
            {'Algorithm': 'Scrypt',
             'CoinName': 'Litecoin',
             'FullName': 'Litecoin (LTC)',
             'FullyPremined': '0',
             'Id': '3808',
             'ImageUrl': '/media/19782/litecoin-logo.png',
             'Name': 'LTC',
             'PreMinedValue': 'N/A',
             'ProofType': 'PoW',
             'SortOrder': '3',
             'Sponsored': False,
             'Symbol': 'LTC',
             'TotalCoinSupply': '84000000',
             'TotalCoinsFreeFloat': 'N/A',
             'Url': '/coins/ltc/overview'},
            'IOT':
            {'Algorithm': 'N/A',
             'CoinName': 'IOTA',
             'FullName': 'IOTA (IOT)',
             'FullyPremined': '1',
             'Id': '127356',
             'ImageUrl': '/media/1383540/iota_logo.png',
             'Name': 'IOT',
             'PreMinedValue': 'N/A',
             'ProofType': 'Tangle',
             'SortOrder': '1247',
             'Sponsored': False,
             'Symbol': 'IOT',
             'TotalCoinSupply': '2779530283',
             'TotalCoinsFreeFloat': 'N/A',
             'Url': '/coins/iot/overview'}}


def raw_price_template(price=7000.00, low=6800.00, high=7200.00):
    return {'CHANGE24HOUR': -297.72999999999956,
            'CHANGEDAY': 10.510000000000218,
            'CHANGEPCT24HOUR': -4.11660843342675,
            'CHANGEPCTDAY': 0.1517871456073467,
            'FLAGS': '1',
            'FROMSYMBOL': 'BTC',
            'HIGH24HOUR': high,
            'HIGHDAY': 7017.99,
            'LASTMARKET': 'Kraken',
            'LASTTRADEID': '1521994152.0339',
            'LASTUPDATE': 1521994152,
            'LASTVOLUME': 0.0131976,
            'LASTVOLUMETO': 91.52667576,
            'LOW24HOUR': low,
            'LOWDAY': 6811.89,
            'MARKET': 'CCCAGG',
            'MKTCAP': 117465330951,
            'OPEN24HOUR': 7232.41,
            'OPENDAY': 6924.17,
            'PRICE': price,
            'SUPPLY': 16938825,
            'TOSYMBOL': 'EUR',
            'TOTALVOLUME24H': 420193.2637329436,
            'TOTALVOLUME24HTO': 2914491767.1551404,
            'TYPE': '5',
            'VOLUME24HOUR': 9936.121144569997,
            'VOLUME24HOURTO': 69489765.59039718,
            'VOLUMEDAY': 5612.430257430866,
            'VOLUMEDAYTO': 38821131.9139348}


def display_price_template(price='€ 7,000.00', low='€ 6,800.00',
                           high='€ 7,200.00'):
    return {'CHANGE24HOUR': '€ -297.73',
            'CHANGEDAY': '€ 10.51',
            'CHANGEPCT24HOUR': '-4.12',
            'CHANGEPCTDAY': '0.15',
            'FROMSYMBOL': 'Ƀ',
            'HIGH24HOUR': high,
            'HIGHDAY': '€ 7,017.99',
            'LASTMARKET': 'Kraken',
            'LASTTRADEID': '1521994152.0339',
            'LASTUPDATE': 'Just now',
            'LASTVOLUME': 'Ƀ 0.01320',
            'LASTVOLUMETO': '€ 91.53',
            'LOW24HOUR': low,
            'LOWDAY': '€ 6,811.89',
            'MARKET': 'CryptoCompare Index',
            'MKTCAP': '€ 117.47 B',
            'OPEN24HOUR': '€ 7,232.41',
            'OPENDAY': '€ 6,924.17',
            'PRICE': price,
            'SUPPLY': 'Ƀ 16,938,825.0',
            'TOSYMBOL': '€',
            'TOTALVOLUME24H': 'Ƀ 420.19 K',
            'TOTALVOLUME24HTO': '€ 2,914.49 M',
            'VOLUME24HOUR': 'Ƀ 9,936.12',
            'VOLUME24HOURTO': '€ 69,489,765.6',
            'VOLUMEDAY': 'Ƀ 5,612.43',
            'VOLUMEDAYTO': '€ 38,821,131.9'}


def get_price(symbols, unit, full=False):
    if not isinstance(symbols, (list, tuple)):
        symbols = [symbols]

    raw_prices = {}
    for symbol in symbols:
        raw_prices[symbol] = {unit: raw_price_template()}

    return raw_prices
