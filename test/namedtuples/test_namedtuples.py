from src.namedtuple.util import calculate_average_marks


def test_basic_case():
    n = 3
    columns = ["ID", "MARKS", "NAME", "CLASS"]
    records = [
        ["1", "97", "Raymond", "7"],
        ["2", "50", "Steven", "4"],
        ["3", "91", "Aditya", "9"]
    ]
    assert calculate_average_marks(n, columns, records) == 79.33


def test_single_student():
    n = 1
    columns = ["ID", "MARKS"]
    records = [["1", "100"]]
    assert calculate_average_marks(n, columns, records) == 100.00


def test_all_same_marks():
    n = 3
    columns = ["ID", "MARKS"]
    records = [
        ["1", "50"],
        ["2", "50"],
        ["3", "50"]
    ]
    assert calculate_average_marks(n, columns, records) == 50.00


def test_decimal_average():
    n = 4
    columns = ["ID", "MARKS"]
    records = [
        ["1", "10"],
        ["2", "20"],
        ["3", "30"],
        ["4", "40"]
    ]
    assert calculate_average_marks(n, columns, records) == 25.00
