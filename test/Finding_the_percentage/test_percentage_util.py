from src.Finding_the_percentage.util import calculate_average


def test_average_found():
    data = {"Mohan": [90, 80, 70]}
    assert calculate_average(data, "Mohan") == 80.00


def test_average_value():
    data = {"A": [10, 20, 30]}
    assert calculate_average(data, "A") == 20.00


def test_student_not_found():
    data = {"A": [10, 20]}
    assert calculate_average(data, "B") is None
