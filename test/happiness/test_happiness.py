from src.happiness.util import calculate_happiness


def test_basic_case():
    arr = [1, 5, 3]
    A = {3, 1}
    B = {5, 7}

    assert calculate_happiness(arr, A, B) == 1


def test_all_positive():
    arr = [1, 2, 3]
    A = {1, 2, 3}
    B = {4}

    assert calculate_happiness(arr, A, B) == 3


def test_all_negative():
    arr = [4, 5, 6]
    A = {1}
    B = {4, 5, 6}

    assert calculate_happiness(arr, A, B) == -3


def test_mixed_values():
    arr = [1, 2, 3, 4]
    A = {1, 3}
    B = {2, 4}

    assert calculate_happiness(arr, A, B) == 0


def test_none_in_sets():
    arr = [10, 20]
    A = {1}
    B = {2}

    assert calculate_happiness(arr, A, B) == 0
