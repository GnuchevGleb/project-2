def mask_account_card(card_number_account: str) -> str:
    """
    Функция, которая умеет обрабатывать информацию как о картах, так и о счетах
    Примеры работы функции
     Пример для карты
    Visa Platinum 7000792289606361 - входной аргумент
    Visa Platinum 7000 79** **** 6361 - выход функции

     Пример для счета
    Счет 73654108430135874305 - входной аргумент
    Счет **4305 - выход функции
    """
    print(card_number_account)
    if "Счет" in card_number_account:
        if card_number_account[-20:].isdigit():
            from src.masks import get_mask_account  # type: ignore

            return str(f"Счет {(get_mask_account(str(card_number_account[-20:])))}")
        return str("ошибка ввода")

    if "Maestro" or "MasterCard" in card_number_account:
        if card_number_account[-16:].isdigit():
            from src.masks import get_mask_card_number  # type: ignore

            return f"{card_number_account[:-16]}{(get_mask_card_number(str(card_number_account[-16:])))}"
        return str("ошибка ввода")
    assert False


def get_date(date_time_1: str) -> str:
    """
     Функция, которая принимает на вход строку с датой в формате
    "2024-03-11T02:26:18.671407"
      и возвращает строку с датой в формате
     "ДД.ММ.ГГГГ" ("11.03.2024")
    """

    print(len(date_time_1))
    if len(date_time_1) > 0:
        return f"{date_time_1[8:10]}.{date_time_1[5:7]}.{date_time_1[0:4]}"
    return "ошибка формата даты"


# date_time = ""
# print(get_date(date_time))
