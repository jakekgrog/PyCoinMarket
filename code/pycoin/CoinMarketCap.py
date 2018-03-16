import json
import requests

class CoinMarketCap(object):

    def __init__(self, coin="bitcoin"):
        self.c_id = coin

        response = requests.get("https://api.coinmarketcap.com/v1/ticker/" + self.c_id + "/")
        data = json.loads(response.text)[0]

        self.c_name = data['name']
        self.c_symbol = data['symbol']
        self.c_rank = data['rank']
        self.c_price = data['price_usd']
        self.c_btc = data['price_btc']
        self.c_vol_24 = data['24h_volume_usd']
        self.c_market_cap = data['market_cap_usd']
        self.c_avail_supply = data['available_supply']
        self.c_total_supply = data['total_supply']
        self.c_max_supply = data['max_supply']
        self.c_perc_change_hour = data['percent_change_1h']
        self.c_percent_change_day = data['percent_change_24h']
        self.c_perc_change_week = data['percent_change_7d']
        self.c_last_update = data['last_updated']

    def id(self):
        return self.c_id

    def name(self):
        return self.c_name

    def symbol(self):
        return self.c_symbol
    
    def rank(self):
        return self.c_rank
    
    def price(self, currency="usd"):
        return self.c_price

    def price_btc(self):
        return self.c_btc

    def volume(self):
        return self.c_vol_24

    def market_cap(self):
        return self.c_market_cap

    def available(self):
        return self.c_avail_supply

    def total(self):
        return self.c_total_supply

    def max(self):
        return self.c_max_supply

    def percent_change_hour(self):
        return self.c_perc_change_hour

    def percent_change_day(self):
        return self.c_perc_change_day

    def percent_change_week(self):
        return self.c_perc_change_week
    
    def last_update(self):
        return self.c_last_update


def main():
    cmc = CoinMarketCap()
    print(cmc.name())
    cmc2 = CoinMarketCap('ethereum')
    print(cmc2.name())

if __name__=="__main__":
    main()