from src.ftr import list_transactions_csv, list_transactions_ex, list_transactions_json


def test_list_transactions_csv(file_not):
    assert list_transactions_csv(file_not) == ['файл не найден']


def test_list_transactions_csv_2(tst_sv):
    assert type(list_transactions_csv(tst_sv)) == list


def test_list_transactions_ex(file_not):
    assert list_transactions_csv(file_not) == ['файл не найден']


def test_llist_transactions_ex_2(tst_sv):
    assert type(list_transactions_csv(tst_sv)) == list


def test_list_transactions_json(file_not):
    assert list_transactions_csv(file_not) == ['файл не найден']


def test_list_transactions_json_2(tst_sv):
    assert type(list_transactions_csv(tst_sv)) == list