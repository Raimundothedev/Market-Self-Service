import requests
import os
import json
import time
from dotenv import load_dotenv
from dataclasses import dataclass

load_dotenv()

CACHE_FILE = "currency/rates_cache.json"
CACHE_DURATION = 3600 * 24  

def get_conversion_rates():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            cache = json.load(f)

        age = time.time() - cache["timestamp"]
        if age < CACHE_DURATION:
            return cache["conversion_rates"]

    print("Searching in API...")
    url = 'https://v6.exchangerate-api.com/v6/7725f1b0382c0b2969db96d7/latest/USD'
    response = requests.get(url)
    data = response.json()
    conversion_rates = data['conversion_rates']

    with open(CACHE_FILE, "w") as f:
        json.dump({
            "timestamp": time.time(),
            "conversion_rates": conversion_rates
        }, f, indent=4)

    return conversion_rates

@dataclass
class Currency:
    symbol: str
    rate: float
conversion_rates = get_conversion_rates()

symbols = {
    "USD": "$",
    "BRL": "R$",
    "EUR": "€",
    "GBP": "£",
    "JPY": "¥",
    "CNY": "¥",
    "AUD": "A$",
    "CAD": "C$",
    "CHF": "Fr",
    "INR": "₹",
    "MXN": "Mex$",
    "ARS": "AR$",
    "CLP": "CLP$",
    "COP": "COL$",
    "UYU": "$U",
    "PYG": "₲",
    "RUB": "₽",
    "KRW": "₩",
    "TRY": "₺",
    "ZAR": "R",
    "SEK": "kr",
    "NOK": "kr",
    "DKK": "kr",
    "PLN": "zł",
    "CZK": "Kč",
    "HUF": "Ft",
    "ILS": "₪",
    "THB": "฿",
    "VND": "₫",
    "PHP": "₱",
    "IDR": "Rp",
    "MYR": "RM",
    "SGD": "S$",
    "HKD": "HK$",
    "NZD": "NZ$",
    "SAR": "﷼",
    "AED": "د.إ",
    "EGP": "E£",
    "NGN": "₦",
    "PKR": "₨",
    "BDT": "৳",
    "UAH": "₴",
}

currencies = {
    currency: Currency(symbol, conversion_rates[currency])
    for currency, symbol in symbols.items()
}

def to_usd(value, currency):
    if currency not in symbols:
        print("currency not found")
        return
    return round(value / currencies[currency].rate, 2)


def from_usd(value, currency):
    if currency not in symbols:
        print("currency not found")
        return
    return round(value * currencies[currency].rate, 2)

