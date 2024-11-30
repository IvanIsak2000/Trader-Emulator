from secrets import randbits

import requests
from rich.table import Table
from random import randint

from env import CURRENCIES


class MarketGraph:
    def __init__(self):
        self.url = f'https://api.coingecko.com/api/v3/coins/'

    def get_currencies_price(self, currency: str):
        return requests.get(self.url + currency).json()

    def get_currencies_table(self) -> list[Table]:
        table = Table()
        table.add_column(header='Currency', header_style='bold red3')
        table.add_column(header='Name', style='magenta')
        table.add_column(header='Price($)', style='green', justify='right')
        table.add_column(header='24H Range', justify='right')

        for i in CURRENCIES:
            c = self.get_currencies_price(i['id'])
            table.add_row(
                c['symbol'].upper(),
                c['name'],
                str(c['market_data']['current_price']['usd']),
                str(randint(1, 20)) + '%'
            )
        return table

