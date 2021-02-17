class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_change(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать колличество {amount}')


        r = requests.get(f'https://api.exchangeratesapi.io/latest?base={quote_ticker}&symbols={base_ticker}')
        total_base = json.loads(r.content)["rates"][keys[base]] * amount

        return total_base
