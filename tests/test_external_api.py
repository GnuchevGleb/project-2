from requests import patch

from src.external_api import currency_exchange_rate


def test_currency_exchange_rate():
    # """
    # функция Mock для API обращение к серверу обмена валют для RUB
    # """
    assert currency_exchange_rate("RUB") == 1


def test_currency_exchange_rate_1():
    # """
    # функция Mock для API обращение к серверу обмена валют для RUB
    # """
    assert currency_exchange_rate(5) == 0
