import csv
import requests
from datetime import datetime

def get_rate(cur_code):
    response_currency = requests.get(f'https://api.nbp.pl/api/exchangerates/rates/A/{cur_code}/?format=json')
    currency_rate = response_currency.json()['rates'][0]["mid"]
    return currency_rate

def save_rate(currency_rate, cur_code):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('currency.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([timestamp, f"{cur_code}",f"{currency_rate:.4f}".replace('.',',')])
