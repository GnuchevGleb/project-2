import os

import requests
from dotenv import load_dotenv


def currency_exchange_rate(currencys: str) -> float:
    """Функция конвертации валюты"""

    try:
        # Загрузка переменных из .env-файла
        load_dotenv()

        ###############################################################################
        # Получение значения переменной API_KEY из .env-файла
        kei_api = os.getenv("API_KEY")
        len(currencys)
        # Отправка GET-запроса к API

        url_rub_currencys = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base={currencys}"
        headers = {"apikey": kei_api}
        response_rub_currencys = requests.get(url_rub_currencys, headers=headers)
        print(response_rub_currencys.json())  # вывод ответа от сервера курса валют
        response_rub_currencys = response_rub_currencys.json()
        print(response_rub_currencys)
        ################################################################################
        # результат для проверки функциональности Api возвращает данные вида:
        # response_rub_currencys = {
        #     "success": True,
        #     "timestamp": 1741618864,
        #     "base": "USD",
        #     "date": "2025-03-10",
        #     "rates": {"RUB": 87.873766},
        # }
        #################################################################################

        for response_rub_currencys_key, response_rub_currencys_value in response_rub_currencys.items():

            if response_rub_currencys_key == "rates":
                currency_currencys = float(f'{response_rub_currencys_value.get("RUB"): .2f}')
                print(f" курс {currencys} =  {currency_currencys}")
                return currency_currencys
    except TypeError:
        print("ошибка типа данных")
        return 0
    assert False


print(currency_exchange_rate("USD"))
