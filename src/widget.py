from masks import get_mask_account
from masks import get_mask_card_number

def mask_account_card(bank_account: str) -> str:
    """Функция, которая обрабатывает информацию о картах и счетах"""
    if 'Счет' in bank_account:
        bank_account_account = get_mask_account(bank_account[-20:])
        return (f'Счет {bank_account_account}')
    else:
        bank_account_card = get_mask_card_number(bank_account[-16:])
        return (f'{bank_account[0:-17]} {bank_account_card}')


print(mask_account_card('Maestro 1596837868705199'))
print(mask_account_card('Счет 64686473678894779589'))
print(mask_account_card('MasterCard 7158300734726758'))
print(mask_account_card('Счет 35383033474447895560'))
print(mask_account_card('Visa Classic 6831982476737658'))
print(mask_account_card('Visa Platinum 8990922113665229'))
print(mask_account_card('Visa Gold 5999414228426353'))
print(mask_account_card('Счет 73654108430135874305'))


def get_date(date_today: str) -> str:
    """Функция, которая принимает на вход строку с датой"""
    day = date_today[8:10]
    month = date_today[5:7]
    year = date_today[0:4]
    return (f'{day}.{month}.{year}')


print(get_date('2024-03-11T02:26:18.671407'))