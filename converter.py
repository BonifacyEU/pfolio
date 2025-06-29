import csv
import requests
from datetime import datetime



def save_eur_rate():
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    response_eur = requests.get('https://api.nbp.pl/api/exchangerates/rates/A/EUR/?format=json')
    eur_rate = response_eur.json()['rates'][0]["mid"]

    with open('currency.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([timestamp, f"{eur_rate:.4f}".replace('.',',')])
