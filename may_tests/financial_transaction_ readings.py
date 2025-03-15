import csv
import os

from dotenv import load_dotenv

# определяем путь к файлу с транзакциями
load_dotenv()
way = os.getenv("WAY_TRANSACTION_CSV")


def list_transactions_csv(ways:str)->dict:

    """функция считывания финансовых операций из CSV файла"""

    print(ways)
    with open(ways, "r", encoding="utf-8") as file:  # Открываем файл
        text = csv.DictReader(file, delimiter=";")
        try:
            for rows in text:
                if rows["id"].isdigit() == True:
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


list_tr_csv = list_transactions_csv(way)
