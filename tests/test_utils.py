from unittest.mock import Mock


def test_transaction():
    mock_transaction = Mock(
        return_value=r"C:\Users\sanya\PycharmProjects\python_project_dz2\data\operations.json"
    )
    transaction = mock_transaction
    transaction(
        file_json=r"C:\Users\sanya\PycharmProjects\python_project_dz2\data\operations.json"
    ) == r"C:\Users\sanya\PycharmProjects\python_project_dz2\data\operations.json"
    mock_transaction.assert_called_once_with(
        file_json=r"C:\Users\sanya\PycharmProjects\python_project_dz2\data\operations.json"
    )
