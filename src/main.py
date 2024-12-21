from tarfile import data_filter

from src.utils import transaction
from src.financial_transaction import transactions_csv_file, transactions_xlsx_file
from src.processing import filter_by_state, sort_by_date
from src.main_project_logic import rub_transactions, filter_transactions

def main():
    '''Функция, которая отвечает за основную логику проекта и связывает функциональности между собой.'''

    print('''Привет! Добро пожаловать в программу работы с банковскими транзакциями.
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла''')

    # Пользователь выбирает откуда получает информацию
    user_answer_1 = int(input('Выберите пункт: '))

    if user_answer_1 == 1:
        read_file = transaction("..\\data\\operations.json")
        print('Для обработки выбран JSON-файл')
    elif user_answer_1 == 2:
        read_file = transactions_csv_file("..\\files\\transactions.csv")
        print('Для обработки выбран CSV-файл')
    elif user_answer_1 == 3:
        read_file = transactions_xlsx_file("..\\files\\transactions_excel.xlsx")
        print('Для обработки выбран XLSX-файл')
    else:
        print('Ошибка!')

    # Пользователь выбирает статус интересующих его операций
    while True:
        print('''Введите статус, по которому необходимо выполнить фильтрацию.
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.''')

        user_answer_2 = str(input('Введите статус: ')).upper()
        if user_answer_2 == 'EXECUTED' or user_answer_2 == 'CANCELED' or user_answer_2 == 'PENDING':
            filter_file = filter_by_state(read_file, user_answer_2)
            break
        else:
            print(f'Статус операции "{user_answer_2}" недоступен.')

    # Уточнения выборки операций
    # 1 и 2
    while True:
        print('Отсортировать операции по дате? Да/Нет')
        user_answer_3 = str(input('')).lower()
        if user_answer_3 == 'да':
            while True:
                print('Отсортировать по возрастанию или по убыванию?')
                user_answer_4 = str(input('')).lower()
                if user_answer_4 == 'по возрастанию':
                    data_file = sort_by_date(filter_file, False)
                    break
                elif user_answer_4 == 'по убыванию':
                    data_file = sort_by_date(filter_file, True)
                    break
                else:
                    print('Некорректно введен запрос')
            break
        elif user_answer_3 == 'нет':
            data_file = filter_file
            break

    #3
    while True:
        print('Выводить только рублевые тразакции? Да/Нет')
        user_answer_5 = str(input('')).lower()
        if user_answer_5 == 'да':
            transactions = rub_transactions(data_file)
            break
        elif user_answer_5 == 'нет':
            transactions = data_file
            break

    #4
    while True:
        print('Отфильтровать список транзакций по определенному слову в описании? Да/Нет')
        user_answer_6 = str(input('')).lower()
        if user_answer_6 == 'да':
            word_search = str(input('Введите слово для фильтрации: ')).lower()
            transactions_f = filter_transactions(transactions, word_search)
            break
        elif user_answer_6 == 'нет':
            transactions_f = transactions
            break

    #Итог
    print('Распечатываю итоговый список транзакций...')
    if len(transactions_f) == 0:
        print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')
    else:
        print(f'{transactions_f}')
        print(f'Всего банковских операций в выборке: {len(transactions_f)}')


main()