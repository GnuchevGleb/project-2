import csv
import json
import os

import pandas as pd


current_dir = os.path.dirname(__file__)
data_dir = os.path.join(current_dir, "..", "data")
print(data_dir)  # путь до директории data

way_json = os.path.join(data_dir, "operations.json")
way_csv = os.path.join(data_dir, "transactions.csv")
way_ex = os.path.join(data_dir, "transactions_excel.xlsx")


def list_transactions_csv(ways: str) -> list:
    """функция считывания финансовых операций из CSV файла"""
    ways = str(ways)
    try:
        with open(ways, "r", encoding="utf-8") as file:  # Открываем файл
            text = list(csv.DictReader(file, delimiter=";"))
    except FileNotFoundError:
        text = ["файл не найден"]
    except TypeError:
        text = ["Ошибка"]
    # print('****',text)
    return text


# list_tr_csv = list_transactions_csv(way_csv)


def list_transactions_ex(ways: str) -> list:
    """функция считывания финансовых операций из XLCX файла"""
    ways = str(ways)
    try:
        text = pd.read_excel(ways)
        text = text.to_dict(orient="records")

    except FileNotFoundError:
        text = ["файл не найден"]
    except TypeError:
        text = ["Ошибка"]
    # print(text)
    return list(text)


# list_tr_ex = list_transactions_ex(way_ex)


def list_transactions_json(ways: str) -> list:
    """функция считывания финансовых операций из json файла"""

    ways = str(ways)
    try:
        with open(ways, "r", encoding="utf-8") as file:  # Открываем файл
            text = file.read()  # Читаем содержимое в переменную text
            text = json.loads(text)

    except FileNotFoundError:
        text = ["файл не найден"]
    except TypeError:
        text = ["Ошибка"]
    # print(text)
    return text


# list_tr_ex_json = list_transactions_json(way_json)

# if __name__ == '__main__':
#     list_tr_csv = list_transactions_csv(way_csv)
#     list_tr_ex = list_transactions_ex(way_ex)
#     list_tr_ex_json = list_transactions_json(way_json)
# #
# #
# print(list_tr_ex_json,'list_tr_json')
