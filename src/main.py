import os


from src.ftr import list_transactions_csv, list_transactions_ex, list_transactions_json
from src.sort_description import sort_description
from src.sort_list import sort_list


current_dir = os.path.dirname(__file__)
data_dir = os.path.join(current_dir, "..", "data")
print(data_dir)  # путь до директории data

way_json = os.path.join(data_dir, "operations.json")
way_csv = os.path.join(data_dir, "transactions.csv")
way_ex = os.path.join(data_dir, "transactions_excel.xlsx")

print(f"Привет! \nДобро пожаловать в программу работы с банковскими транзакциями. ")
print(
    f"Выберите необходимый пункт меню:"
    f"\n1. Получить информацию о транзакциях из JSON-файла"
    f"\n2. Получить информацию о транзакциях из CSV-файла"
    f"\n3. Получить информацию о транзакциях из XLSX-файла"
)


def choice_user(choice: str):
    """функция проверяет правильность ввода данных пользователем"""

    user_input = input("Введите число от 1 до 3 чтобы продолжить: ")
    while user_input not in ["1", "2", "3"]:
        user_input = input("Введите число от 1 до 3 чтобы продолжить: ")
    #################################################################################################################
    #                                                       обработка  JSON-файла
    if user_input == "1":
        print("Для обработки выбран JSON-файл.")
        text_json = list_transactions_json(way_json)

        transactions_list = text_json
    ##################################################################################################################
    #                                                             обработка CSV-файла
    elif user_input == "2":
        print("Для обработки выбран CSV-файл.")
        text_csv = list_transactions_csv(way_csv)

        lists_transactjon_csv = []
        try:
            for rows in text_csv:
                if rows["id"].isdigit():
                    dict_transactjon_csv = {
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

                    lists_transactjon_csv.append(dict_transactjon_csv)
                else:
                    print("исключена строка с не числовым значением id")

        except ValueError:
            print(False)  # Если строка не может быть преобразована

        transactions_list = lists_transactjon_csv
    #############################################################################################################
    #                                                             обработка XLSX-файла
    elif user_input == "3":
        print("Для обработки выбран XLSX-файл.")
        text_ex = list_transactions_ex(way_ex)
        lists_transactions_ex = []
        try:
            for rows in text_ex:

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

                    lists_transactions_ex.append(dict_transactjon_ex)
                else:
                    print("исключена строка с не числовым значением id")
        except ValueError:
            print(False)  # Если строка не может быть преобразована

        transactions_list = lists_transactions_ex
    #################################################################################################################
    print(
        f"Введите статус, по которому необходимо выполнить фильтрацию."
        f"\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING "
    )

    user_input_category = input("Введите статус чтобы продолжить: ")
    user_input_category = user_input_category.upper()
    while user_input_category not in ["EXECUTED", "CANCELED", "PENDING"]:
        print(f'Статус операции "{user_input_category}" недоступен.')
        user_input_category = input("Введите статус чтобы продолжить: ")

    sorting_list = sort_list(user_input_category, transactions_list)
    print(sorting_list)
    print(f" Найдено {len(sorting_list)} операций по заданным критериям")

    print(f"{sort_description(sorting_list)}")

    return


choice_user(" Выбор варианта ")
