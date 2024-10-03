#три прямі на одному графіку, з євро, доларем та фунтом стерлінгів

import requests
import matplotlib.pyplot as plt

API = "https://bank.gov.ua/NBU_Exchange/exchange_site?start=20240920&end=%2020241003&json"

usd = requests.get(API+"&valcode=usd").json()
eur = requests.get(API+"&valcode=eur").json()
gbp = requests.get(API+"&valcode=gbp").json()


def extract_data(data):
    dates = [item['exchangedate'][:5] for item in data]
    rates = [item['rate'] for item in data]
    return dates, rates


usd_dates, usd_rates = extract_data(usd)
eur_dates, eur_rates = extract_data(eur)
gbp_dates, gbp_rates = extract_data(gbp)

plt.figure(figsize=(12, 6))
plt.plot(usd_dates, usd_rates, label='USD', color='blue')
plt.plot(eur_dates, eur_rates, label='EUR', color='green')
plt.plot(gbp_dates, gbp_rates, label='GBP', color='red')

plt.xlabel('Дата')
plt.ylabel('Курс валют')
plt.title('Курс USD, EUR та GBP до гривні за минулі два тижні')
plt.legend()
plt.grid(True)
plt.show()