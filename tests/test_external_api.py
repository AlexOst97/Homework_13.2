import os
from unittest.mock import patch

from dotenv import load_dotenv

from src.external_api import sum_transactions

load_dotenv()
API_KEY = os.getenv("API_KEY")
headers = {"apikey": API_KEY}


# для test_sum_transactions_1 c USD
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
answer_1 = {
    "success": True,
    "query": {"from": "USD", "to": "RUB", "amount": 31957.58},
    "info": {"timestamp": 1733651235, "rate": 98.813295},
    "date": "2024-12-08",
    "result": 3157833.780026,
}


@patch("requests.get")
def test_sum_transactions_1(mock_get):
    mock_get.return_value.json.return_value = answer_1
    assert sum_transactions(transaction_1) == 3157833.780026
    mock_get.assert_called_once()
    mock_get.assert_called_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=31957.58",
        headers=headers,
    )


# для test_sum_transactions_2 c EUR
transaction_2 = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
        "amount": "31957.58",
        "currency": {"name": "руб.", "code": "EUR"},
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589",
}
answer_2 = {
    "success": True,
    "query": {"from": "USD", "to": "RUB", "amount": 31957.58},
    "info": {"timestamp": 1733651235, "rate": 98.813295},
    "date": "2024-12-08",
    "result": 3339677.843015,
}


@patch("requests.get")
def test_sum_transactions_2(mock_get):
    mock_get.return_value.json.return_value = answer_2
    assert sum_transactions(transaction_1) == 3339677.843015
    mock_get.assert_called_once()
    mock_get.assert_called_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=31957.58",
        headers=headers,
    )


# для test_sum_transactions_3 c RUB
transaction_3 = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
        "amount": "31957.58",
        "currency": {"name": "руб.", "code": "RUB"},
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589",
}


def test_sum_transactions_3():
    assert sum_transactions(transaction_3) == "31957.58"
