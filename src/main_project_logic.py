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
        if pattern.search(transaction["description"]):
            list_dict.append(transaction)
    return list_dict


def returned_description(
    transaction_list: list[dict], description_list: list[str]
) -> dict:
    """Функция, которая будет принимать список словарей с данными о банковских операциях и список категорий операций, а возвращать словарь, в котором ключи — это названия категорий"""
    list_for_requirement = []
    for description in description_list:
        for transaction in transaction_list:
            if transaction["description"] == description.title():
                list_for_requirement.append(transaction["description"])
    returned_dict = Counter(list_for_requirement)
    return returned_dict


def rub_transactions(transactions: list) -> list:
    """Функция, которая выводить только рублевые тразакции"""
    rub_list = []
    for transaction in transactions:
        if "currency_code" in transaction and transaction["currency_code"] == "RUB":
            rub_list.append(transaction)
            return rub_list
        elif (
            "operationAmount" in transaction
            and transaction["operationAmount"]["currency"]["code"] == "RUB"
        ):
            rub_list.append(transaction)
            return rub_list
    return ""
