def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""
    return card_number[0:4] + " " + card_number[4:6] + "**" + " " + "****" + " " + card_number[12:]


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера банковского счета"""
    return "**" + account_number[16:]


#print(get_mask_card_number("7000792289606361"))
#print(get_mask_account("73654108430135874305"))
