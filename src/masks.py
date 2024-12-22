import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(
    r"C:\Users\sanya\PycharmProjects\python_project_dz2\logs\masks.log",
    "w",
    encoding="utf-8",
)
file_formatter = logging.Formatter(
    "%(asctime)s - %(funcName)s - %(levelname)s: %(message)s)"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""
    if len(card_number) == 16:
        logger.info(
            card_number[0:4]
            + " "
            + card_number[4:6]
            + "**"
            + " "
            + "****"
            + " "
            + card_number[12:]
        )
        return (
            card_number[0:4]
            + " "
            + card_number[4:6]
            + "**"
            + " "
            + "****"
            + " "
            + card_number[12:]
        )
    else:
        logger.error("Ошибка ввода")
    return ""


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера банковского счета"""
    if len(account_number) == 20:
        logger.info("**" + account_number[16:])
        return "**" + account_number[16:]
    else:
        logger.error("Ошибка ввода")
    return ""


# print(get_mask_card_number("7000792289606361"))
# print(get_mask_account("73654108430135874305"))
