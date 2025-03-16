import re
import json
import logging


logger = logging.getLogger("sort_list.py")
file_handler = logging.FileHandler("../logs/sort_list.py", "w")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def sort_list(pattern: str, list_sort: list) -> list:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка"""

    logger.info(pattern)
    sorting_list = []
    for row in list_sort:
        row = json.dumps(row)
        if re.findall(pattern, row, flags=0):
            row = json.loads(row)

            sorting_list.append(row)

    logger.info(type(sorting_list))
    logger.info(sorting_list)
    return sorting_list
