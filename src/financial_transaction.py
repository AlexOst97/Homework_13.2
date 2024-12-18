import csv
from typing import Any

import pandas as pd


def transactions_csv_file(filename: str) -> Any:
    """Функция, считывающая финансовые операции из CSV-файлов"""
    transactions_csv = []
    try:
        with open(f"{filename}", encoding="utf-8") as file_csv:
            reader = csv.DictReader(file_csv, delimiter=";")
            for row in reader:
                transactions_csv.append(row)
            return transactions_csv
    except Exception as error:
        return f"Ошибка: {error}"
    return ""


print(transactions_csv_file("..\\files\\transactions.csv"))


def transactions_xlsx_file(filename: str) -> Any:
    """Функция, считывающая финансовые операции из XLSX-файлов"""
    try:
        excel_file = pd.read_excel(f"{filename}")
        transactions_xlsx = excel_file.to_dict(orient="records")
        return transactions_xlsx
    except Exception as error:
        return f"Ошибка: {error}"
    return ""


print(transactions_xlsx_file("..\\files\\transactions_excel.xlsx"))
