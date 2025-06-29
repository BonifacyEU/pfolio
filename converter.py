import csv
from datetime import datetime


def save_timestamp():
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open('dates.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([timestamp])
