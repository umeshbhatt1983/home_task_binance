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
    def get_spread_delta(self, asset, field, output=False):

        delta = {}
        old_spread = self.get_price_spread(asset, field)
        time.sleep(10)
        new_spread = self.get_price_spread(asset, field)

        for key in old_spread:
            delta[key] = abs(old_spread[key]-new_spread[key])

        for key in delta:
            self.prom_gauge.labels(key).set(delta[key])

        if output:
            print("\n Absolute Delta for %s" % asset )
            print(delta)