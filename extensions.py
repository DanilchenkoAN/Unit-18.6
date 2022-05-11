import requests
import json
from config import keys

class APIException(Exception):
    pass

class CurrencyConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
              
        if quote == base:
            raise APIException (f'Невозможно конвертировать одинаковые валюты {base}')
        
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException (f'Не удалось обработать валюту {quote}')

        try:    
            base_ticker = keys[base]
        except ValueError:
            raise APIException (f'Не удалось обработать валюту {base}')

        try:    
            amount = float(amount)
        except KeyError:
            raise APIException (f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content) [keys[base]] * amount
        total_base = float('{:.2f}'.format(total_base))
        
        return total_base
