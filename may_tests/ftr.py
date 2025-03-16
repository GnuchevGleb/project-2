import csv
import json
import os

import pandas as pd
from dotenv import load_dotenv

# определяем путь к файлу с транзакциями
current_dir = os.path.dirname(__file__)
data_dir = os.path.join(current_dir, '..', 'data')
print(data_dir) # путь до директории data

way_json = os.path.join(data_dir, 'operations.json')
way_csv = os.path.join(data_dir, 'transactions.csv')
way_ex = os.path.join(data_dir, 'transactions_excel.xlsx')


def list_transactions_csv(ways: str) -> dict or str:

    """функция считывания финансовых операций из CSV файла"""

    dict_transactjon = {}
    if os.path.exists(ways):
        print("Path exists")
    else:
        print("Path does not exist")
        return "Path does not exist"

    with open(ways, "r", encoding="utf-8") as file:  # Открываем файл
        text = csv.DictReader(file, delimiter=";")
        print(text)
        try:
            for rows in text:
                if rows["id"].isdigit():
                    dict_transactjon = {
                        "id": int(rows["id"]),
                        "state": rows["state"],
                        "date": rows["date"],
                        "operationAmount": {
                            "amount": rows["amount"],
                            "currency": {"name": rows["currency_name"], "code": rows["currency_code"]},
                        },
                        "description": rows["description"],
                        "from": rows["from"],
                        "to": rows["to"],
                    }
                    print(dict_transactjon)
                else:
                    print("исключена строка с не числовым значением id")

        except ValueError:
            print(False)  # Если строка не может быть преобразована

    return dict_transactjon
    ##########################################################


list_tr_csv = list_transactions_csv(way_csv)


load_dotenv()
way_ex = os.getenv("WAY_TRANSACTION_XLCX")


def list_transactions_ex(ways: str) -> dict or str:
    """функция считывания финансовых операций из XLCX файла"""

    dict_transactjon_ex = {}
    if os.path.exists(ways):
        print("Path exists")
    else:
        print("Path does not exist")
        return "Path does not exist"

        # with (ways, "r") as file:  # Открываем файл
    text = pd.read_excel(ways)
    text_dic = text.to_dict(orient="records")
    try:
        for rows in text_dic:
            if rows["id"].is_integer():
                dict_transactjon_ex = {
                    "id": int(rows["id"]),
                    "state": rows["state"],
                    "date": rows["date"],
                    "operationAmount": {
                        "amount": rows["amount"],
                        "currency": {"name": rows["currency_name"], "code": rows["currency_code"]},
                    },
                    "description": rows["description"],
                    "from": rows["from"],
                    "to": rows["to"],
                }
                print(dict_transactjon_ex)

            else:
                print("исключена строка с не числовым значением id")
    except ValueError:
        print(False)  # Если строка не может быть преобразована

    return dict_transactjon_ex

###list_tr_ex = list_transactions_ex(way_ex)



load_dotenv()
way_json = os.getenv("WAY_TRANSACTION_JSON")
def list_transactions_json(ways: str) -> dict or str:
    """функция считывания финансовых операций из json файла"""

    with open(ways, "r", encoding="utf-8") as file:  # Открываем файл
        text = file.read()  # Читаем содержимое в переменную text
        text = json.loads(text)
        print(text)


#list_tr_ex_json = list_transactions_json(way_json)