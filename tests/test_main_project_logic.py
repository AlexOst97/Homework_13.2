import pytest
from src.main_project_logic import filter_transactions, returned_description

answer_1 = [{'id': '593027', 'state': 'CANCELED', 'date': '2023-07-22T05:02:01Z', 'amount': '30368', 'currency_name': 'Shilling', 'currency_code': 'TZS', 'from': 'Visa 1959232722494097', 'to': 'Visa 6804119550473710', 'description': 'Перевод с карты на карту'}, {'id': '3176764', 'state': 'CANCELED', 'date': '2022-08-24T14:32:38Z', 'amount': '16652', 'currency_name': 'Euro', 'currency_code': 'EUR', 'from': 'Mastercard 8387037425051294', 'to': 'American Express 5556525473658852', 'description': 'Перевод с карты на карту'}]


@pytest.mark.parametrize("dict_transactions, search_string, expected", answer_1)
def test_filter_transactions(dict_transactions, search_string, expected):
    assert filter_transactions(dict_transactions, search_string) == expected


