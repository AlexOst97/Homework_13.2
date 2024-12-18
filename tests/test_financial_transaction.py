from unittest.mock import Mock

from src.financial_transaction import (transactions_csv_file,
                                       transactions_xlsx_file)


# для transactions_csv_file
def test_transactions_csv_file_1():
    mock_transactions_csv_file = Mock(return_value=r"..\\files\\transactions.csv")
    transactions_csv_file = mock_transactions_csv_file
    transactions_csv_file(
        file_json=r"..\\files\\transactions.csv"
    ) == r"..\\files\\transactions.csv"
    mock_transactions_csv_file.assert_called_once_with(
        file_json=r"..\\files\\transactions.csv"
    )


def test_transactions_csv_file_2():
    assert (
        transactions_csv_file("") == "Ошибка: [Errno 2] No such file or directory: ''"
    )


# для transactions_xlsx_file
def test_transactions_xlsx_file_1():
    mock_transactions_xlsx_file = Mock(
        return_value=r"..\\files\\transactions_excel.xlsx"
    )
    transactions_xlsx_file = mock_transactions_xlsx_file
    transactions_xlsx_file(
        file_json=r"..\\files\\transactions_excel.xlsx"
    ) == r"..\\files\\transactions_excel.xlsx"
    mock_transactions_xlsx_file.assert_called_once_with(
        file_json=r"..\\files\\transactions_excel.xlsx"
    )


def test_transactions_xlsx_file_2():
    assert (
        transactions_xlsx_file("") == "Ошибка: [Errno 2] No such file or directory: ''"
    )
