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
    def get_notional_value(self, asset, field, output=False):
        """
        Return the total notional value of the
        200 bids and asks on each symbol's order book
        in dictionary format.

        """
        uri = "/v3/depth" 

        symbols = self.get_top_symbols(asset, field, output=False)
        notional_list = {}

        for s in symbols['symbol']:
            payload = { 'symbol' : s, 'limit' : 500 }
            r = requests.get(self.API_URL + uri, params=payload)
            for col in ["bids", "asks"]:
                df = pd.DataFrame(data=r.json()[col], columns=["price", "quantity"], dtype=float)
                df = df.sort_values(by=['price'], ascending=False).head(200)
                df['notional'] = df['price'] * df['quantity']
                df['notional'].sum()
                notional_list[s + '_' + col] = df['notional'].sum()

        if output:
            print("\n Total Notional value of %s by %s" %  (asset, field))
            print(notional_list)

        return notional_list