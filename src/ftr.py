import csv
import json

import pandas as pd

way_json = "/home/gleb/PycharmProjects/PythonProject22/data/operations.json"  # путь к файлу json
way_csv = "/home/gleb/PycharmProjects/PythonProject22/data/transactions.csv"  # путь к файлу csv
way_ex = "/home/gleb/PycharmProjects/PythonProject22/data/transactions_excel.xlsx"  # путь к файлу xlsx


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

    return text


list_tr_csv = list_transactions_csv(way_csv)



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

    return list(text)


list_tr_ex = list_transactions_ex(way_ex)



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

    return text


list_tr_ex_json = list_transactions_json(way_json)

