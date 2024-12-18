import os

import requests
from dotenv import load_dotenv


def sum_transactions(transaction: dict) -> type[float]:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    code = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]
    if code == "RUB":
        return amount
    elif code == "USD" or code == "EUR":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code}&amount={amount}"
        load_dotenv()
        API_KEY = os.getenv("API_KEY")
        headers = {"apikey": API_KEY}
        response = requests.get(url, headers=headers)
        data = response.json()
        return data["result"]
    return float


transaction_1 = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
        "amount": "31957.58",
        "currency": {"name": "руб.", "code": "USD"},
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589",
}

print(sum_transactions(transaction_1))
