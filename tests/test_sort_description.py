from src.sort_description import sort_description


def test_sort_description(tst_sv):
    assert type(sort_description(tst_sv)) == dict

def test_sort_description_1(test_transactions):
    assert sort_description(test_transactions) == {'Перевод организации': 2, 'Перевод с карты на карту': 1, 'Перевод со счета на счет': 2}


def test_sort_description_2(test_transactions):
    assert type(sort_description(test_transactions)) == dict