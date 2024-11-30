import os

CLEAR = 'clear' if getattr(os.uname(), 'sysname') == 'Linux' else 'cls'
CURRENCIES = [
    {
        'id': 'bitcoin',
        'symbol': 'BTC',
        'name': 'Bitcoin'
    }

]

API_TOKEN = ''  # Telegram bot API TOKEN
