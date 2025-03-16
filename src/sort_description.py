from collections import Counter


def sort_description(sorting_list: list) -> dict:
    """функция принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий, а значения
     — это количество операций в каждой категории.
       Категории операций хранятся в поле description"""

    description_list = []
    for row in sorting_list:
        description_list.append(row.get("description"))

    counted = Counter(description_list)

    return dict(counted)
