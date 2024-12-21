import re
from collections import Counter

def filter_transactions(dict_transactions: list, search_string: str) -> list:
    """
    Функция, которая будет принимать список словарей с данными о банковских операциях и строку поиска,
    а возвращать список словарей, у которых в описании есть данная строка.
    """
    pattern = re.compile(search_string)
    list_dict = []
    for transaction in dict_transactions:
        if pattern.search(transaction['description']):
            list_dict.append(transaction)
    return list_dict


def returned_description(transaction_list: list[dict], description_list: list[str]) -> dict:
    """Функция, которая будет принимать список словарей с данными о банковских операциях и список категорий операций, а возвращать словарь, в котором ключи — это названия категорий """
    list_for_requirement = []
    for description in description_list:
        for transaction in transaction_list:
            if transaction["description"] == description.title():
                list_for_requirement.append(transaction["description"])
    returned_dict = Counter(list_for_requirement)
    return returned_dict


def rub_transactions(transactions: list) -> list:
  rub_list = []
  for transaction in transactions:
    if 'currency_code' in transaction and transaction['currency_code'] == 'RUB':
        rub_list.append(transaction)
        return rub_list
    elif 'operationAmount' in transaction and transaction["operationAmount"]["currency"]["code"] == 'RUB':
        rub_list.append(transaction)
        return rub_list
  return ''


test_list_1 = [{'id': '593027', 'state': 'CANCELED', 'date': '2023-07-22T05:02:01Z', 'amount': '30368', 'currency_name': 'Shilling', 'currency_code': 'TZS', 'from': 'Visa 1959232722494097', 'to': 'Visa 6804119550473710', 'description': 'Перевод с карты на карту'}, {'id': '5380041', 'state': 'CANCELED', 'date': '2021-02-01T11:54:58Z', 'amount': '23789', 'currency_name': 'Peso', 'currency_code': 'UYU', 'from': '', 'to': 'Счет 23294994494356835683', 'description': 'Открытие вклада'}, {'id': '3176764', 'state': 'CANCELED', 'date': '2022-08-24T14:32:38Z', 'amount': '16652', 'currency_name': 'Euro', 'currency_code': 'EUR', 'from': 'Mastercard 8387037425051294', 'to': 'American Express 5556525473658852', 'description': 'Перевод с карты на карту'}]
test_list_2 = ['Перевод с карты на карту', 'Открытие вклада']

print(filter_transactions(test_list_1, 'Перевод'))

print(returned_description(test_list_1, test_list_2))



