from typing import Generator


def card_number_generator(start: int, stop: int) -> list[str] | str:
    """
    генератор card_number_generator выдает номера банковских карт в формате
    XXXX XXXX XXXX XXXX, где X — цифра номера карты. Генератор может сгенерировать
    номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999
    """

    if (
        bool(isinstance(start, int))
        and bool(isinstance(stop, int))
        and start <= stop
        and start >= 1
        and stop <= 9999999999999999
    ):
        card_number_list = []
        card_numbers = "0000000000000000"
        for card_number in range(start, stop + 1):
            card_number_gen = card_numbers[: -len(str(card_number))] + str(card_number)
            card_number_format = (
                f"{card_number_gen[0:4]} {card_number_gen[4:8]} {card_number_gen[8:12]} {card_number_gen[12:16]}"
            )
            # yield  card_number_format
            card_number_list.append(card_number_format)
        return list(card_number_list)

    else:
        return str("ошибка")


# starts = 1
# stops = 5
# print(card_number_generator(starts, stops))
# generator = card_number_generator(starts, stops)
# print(next(generator))
# print(next(generator))
# print(next(generator))


def filter_by_currency(transaction_list: list[dict], valute: str = "USD") -> Generator:
    """
    Принимает список словарей, представляющих транзакции. Возвращает по одному словарю из списка, в котором валюта
    операции соответствует заданной (по умолчанию USD, для изменения вторым аргументом надо передать буквенный код
    валюты)
    """
    for transaction in transaction_list:
        if transaction["operationAmount"]["currency"]["code"] == valute:
            # print(transaction)
            yield transaction


def transaction_descriptions(transaction_list: list[dict]) -> Generator:
    """
    Принимает список словарей, представляющих транзакции. Возвращает описания каждой операции из списка по одному
    """
    for transaction in transaction_list:
        yield transaction["description"]
