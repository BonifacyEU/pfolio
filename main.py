from converter import get_rate, save_rate

currency_code = input('Enter currency code (USD, GBP, EUR...): ').upper()
currency_rate = get_rate(currency_code)
save_rate(currency_rate, currency_code)
