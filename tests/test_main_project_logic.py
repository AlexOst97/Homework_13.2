import pytest

from src.main_project_logic import filter_transactions, returned_description


def test_filter_transactions_1(filter_transactions_1):
    assert filter_transactions(filter_transactions_1, "Перевод") == [
        {
            "id": "593027",
            "state": "CANCELED",
            "date": "2023-07-22T05:02:01Z",
            "amount": "30368",
            "currency_name": "Shilling",
            "currency_code": "TZS",
            "from": "Visa 1959232722494097",
            "to": "Visa 6804119550473710",
            "description": "Перевод с карты на карту",
        },
        {
            "id": "3176764",
            "state": "CANCELED",
            "date": "2022-08-24T14:32:38Z",
            "amount": "16652",
            "currency_name": "Euro",
            "currency_code": "EUR",
            "from": "Mastercard 8387037425051294",
            "to": "American Express 5556525473658852",
            "description": "Перевод с карты на карту",
        },
    ]


def test_filter_transactions_2(filter_transactions_2):
    assert filter_transactions(filter_transactions_2, "Открытие") == [
        {
            "id": "5380041",
            "state": "CANCELED",
            "date": "2021-02-01T11:54:58Z",
            "amount": "23789",
            "currency_name": "Peso",
            "currency_code": "UYU",
            "from": "",
            "to": "Счет 23294994494356835683",
            "description": "Открытие вклада",
        }
    ]


def test_filter_transactions_3(filter_transactions_3):
    assert filter_transactions(filter_transactions_3, "Перевод") == []


def test_returned_description_1(returned_description_1):
    assert returned_description(returned_description_1, ["Перевод", "Платеж"]) == (
        {"Перевод": 2, "Платеж": 2}
    )


def test_returned_description_2(returned_description_2):
    assert returned_description(returned_description_2, ["Машина"]) == {}


def test_returned_description_3(returned_description_3):
    assert returned_description(returned_description_3, ["Перевод", "Платеж"]) == {}
