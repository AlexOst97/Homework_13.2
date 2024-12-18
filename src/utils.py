import json
import logging
from typing import Any

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(
    r"C:\Users\sanya\PycharmProjects\python_project_dz2\logs\utils.log",
    "w",
    encoding="utf-8",
)
file_formatter = logging.Formatter(
    "%(asctime)s - %(funcName)s - %(levelname)s: %(message)s)"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def transaction(json_file: str) -> Any:
    """функция, которая принимает на вход путь до JSON-файла и возвращает список словарей
    с данными о финансовых транзакциях"""
    empty_list: list[Any] = []
    if json_file is not list and len(json_file) > 0:
        with open(json_file, "r", encoding="utf-8") as file:
            transactions = json.load(file)
            logger.info(transactions)
            return transactions
    else:
        logger.info(empty_list)
        return empty_list


print(
    transaction(
        r"C:\Users\sanya\PycharmProjects\python_project_dz2\data\operations.json"
    )
)
