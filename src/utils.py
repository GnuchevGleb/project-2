import json
import logging
import os
import random

from dotenv import load_dotenv

from src.external_api import currency_exchange_rate
from src.list_currency import list_currency

logger = logging.getLogger("utils.py")
file_handler = logging.FileHandler("../logs/utils.log", "w")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def dictionary_transactions(wa_ys: str) -> dict:
    """функция считывает данные из файла operations.json в директории data в формате json
    и преобразует в формат python"""
    logger.info("начало работы функции dictionary_transactions")

    try:
        with open(wa_ys, "r", encoding="utf-8") as file:  # Открываем файл
            text = file.read()  # Читаем содержимое в переменную text
            logger.info("читаем содержимое файла в переменную text")
            elements = len(json.loads(text))
            random_number = random.randint(1, elements)
        logger.info("возвращаем случайно выбранную транзакцию")
        logger.info(json.loads(text)[random_number])
        return json.loads(text)[random_number]  # возвращаем случайно выбранную транзакцию
    except FileNotFoundError:
        logger.error("FileNotFoundError")
        print("ошибка FileNotFoundError")
        return {}
    except Exception as e:
        logger.error("ошибка Exception")
        print("Exception", e)
        return {}


# определяем путь к файлу с транзакциями
load_dotenv()
dictionary_tr = dictionary_transactions(os.getenv("WAY_TRANSACTION"))


def transactions_sum(dict_transaction: dict) -> float:
    """функция вычисляет сумму транзакций в рублях. Валюту пересчитывает по курсу"""

    summa_tr = 0
    logger.info("начало работы функции transactions_sum")
    logger.info("рассматриваем транзакцию: ")
    logger.info(dict_transaction)

    print(f" рассматриваем транзакцию: {dict_transaction}")
    if dict_transaction == {}:  # проверяем транзакция пустая или нет
        logger.info("нет транзакции")
        summa_tr = 0
        return summa_tr

    for operation in dict_transaction:  # определяем валюту в транзакции
        if operation == "operationAmount":
            currency = dict_transaction[operation].get("currency").get("code")
            summa_tr = float(dict_transaction[operation].get("amount"))
            print(currency, summa_tr)
            logger.info("валюта транзакции: ")
            logger.info(currency)
            logger.info("сумма транзакции: ")
            logger.info(summa_tr)

    if currency == "RUB":
        logger.info("сумма транзакции в рублях: ")
        logger.info(summa_tr)
        return summa_tr  # возвращаем сумму транзакции в рублях

    if currency in list_currency:  # проверяем есть ли данная валюта в списке конвертируемых
        course_currency = currency_exchange_rate(currency)  # отправляем запрос на конвертацию
        summa_tr = float(f"{(summa_tr * course_currency): .2f}")  # вычисляем транзакцию с учётом курса валюты
        logger.info("сумма транзакции с учётом курса валюты: ")
        logger.info(summa_tr)
        return summa_tr

    else:
        print("эта валюта не может быть конвертирована")
        logger.error("эта валюта не может быть конвертирована")
        summa_tr = 0
        return summa_tr


print("Сумма транзакции  ", transactions_sum(dictionary_tr))
