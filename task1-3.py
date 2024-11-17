import requests
import matplotlib.pyplot as plt

API = "https://bank.gov.ua/NBU_Exchange/exchange_site?start=20240920&end=%2020241003&json"

USD = requests.get(API+"&valcode=USD").json()
EUR = requests.get(API+"&valcode=EUR").json()
CHF = requests.get(API+"&valcode=CHF").json()


def extract_data(data):
    dates = [item["exchangedate"][:5] for item in data]
    rates = [item["rate"] for item in data]
    return dates, rates


USD_dates, USD_rates = extract_data(USD)
EUR_dates, EUR_rates = extract_data(EUR)
CHF_dates, CHF_rates = extract_data(CHF)

plt.figure(figsize=(12, 6))
plt.plot(USD_dates, USD_rates, label='USD', color='blue')
plt.plot(EUR_dates, EUR_rates, label='EUR', color='green')
plt.plot(CHF_dates, CHF_rates, label='CHF', color='red')

plt.xlabel("Дата")
plt.ylabel("Курс валют")
plt.title("Курс USD, EUR та CHF до гривні (20.09.2024-03.10.2024)")
plt.legend()
plt.grid(True)
plt.show()