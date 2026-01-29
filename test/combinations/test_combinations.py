from src.combinations.util import probability_of_a


def test_basic_case():
    n = 4
    letters = ["a", "a", "c", "d"]
    k = 2
    assert probability_of_a(n, letters, k) == 0.8333


def test_single_a():
    n = 3
    letters = ["a", "b", "c"]
    k = 1
    assert probability_of_a(n, letters, k) == 0.3333


def test_no_a():
    n = 4
    letters = ["b", "c", "d", "e"]
    k = 2
    assert probability_of_a(n, letters, k) == 0.0


def test_all_a():
    n = 3
    letters = ["a", "a", "a"]
    k = 2
    assert probability_of_a(n, letters, k) == 1.0


def test_large_case():
    n = 5
    letters = ["a", "b", "c", "a", "d"]
    k = 3
    assert probability_of_a(n, letters, k) > 0
