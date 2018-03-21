

class NotImplemented(Exception):
    pass


class Market(object):

    def get_coins_list(self):
        raise NotImplemented

    def get_coin_price(self, coin):
        raise NotImplemented
