from converter import get_rate, save_rate, exchange_amount

amount = float(input('Enter the amount to convert: '))
currency_code = input('Enter currency code (USD, GBP, EUR...): ').upper()
try:
    currency_rate = get_rate(currency_code)
except Exception as e:
    print("Exchange rate could not be fetched. Check currency code.", e)
    exit()

cur_amount = exchange_amount(amount, currency_rate)
print(f'You can get {cur_amount:.4f} {currency_code} at {currency_rate} and {amount}.')
save_rate(currency_rate, currency_code)
