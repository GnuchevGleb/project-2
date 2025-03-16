

from src.sort_list import sort_list


def test_sort_list(filter_status, test_transactions):

    assert type(sort_list(filter_status, test_transactions)) == list

def test_sort_list_1(filter_status, test_transactions):

    assert (sort_list(filter_status, test_transactions)) == [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689',
             'operationAmount': {'amount': '67314.70', 'currency': {'name': 'руб.', 'code': 'RUB'}},
             'description': 'Перевод организации', 'from': 'Visa Platinum 1246377376343588',
             'to': 'Счет 14211924144426031657'}]