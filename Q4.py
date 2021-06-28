# coding=utf-8

import time
import requests
import pandas as pd

class BinanceClient:

    API_URL = 'https://api.binance.com/api'

    def __init__(self):
        self.API_URL = self.API_URL
        self.prom_gauge = Gauge('absolute_delta_value',
                        'Absolute Delta Value of Price Spread', ['symbol'])
    def get_price_spread(self, asset, field, output=False):
        """
        Return the price spread for each symbols in dictionary format
        
        """

        uri = '/v3/ticker/bookTicker'

        symbols = self.get_top_symbols(asset, field)
        spread_list = {}

        for s in symbols['symbol']:
            payload = { 'symbol' : s }
            r = requests.get(self.API_URL + uri, params=payload)
            price_spread = r.json()
            spread_list[s] = float(price_spread['askPrice']) - float(price_spread['bidPrice'])
 
        if output:
            print("\n Price Spread for %s by %s" %  (asset, field))
            print(spread_list)

        return spread_list


