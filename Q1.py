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

    def get_top_symbols(self, asset, field, output=False):
        """
        Return the top 5 symbols with quote asset BTC
        and the highest volume over the last 24 hours
        in descending order in data frames.
        """
        uri = "/v3/ticker/24hr"

        r = requests.get(self.API_URL + uri)
        df = pd.DataFrame(r.json())
        df = df[['symbol', field]]
        df = df[df.symbol.str.contains(r'(?!$){}$'.format(asset))]
        df[field] = pd.to_numeric(df[field], downcast='float', errors='coerce')
        df = df.sort_values(by=[field], ascending=False).head(5)

        if output:
            print("\n Top Symbols for %s by %s" %  (asset, field))
            print(df)


        return df