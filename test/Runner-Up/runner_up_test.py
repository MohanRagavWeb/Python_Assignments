from src.Runner_Up.util import find_runner_up


def test_runner_up_basic():
    arr = [2, 3, 6, 6, 5]
    assert find_runner_up(arr) == 5


def test_runner_up_negative():
    arr = [-10, -20, -30, -10]
    assert find_runner_up(arr) == -20


def test_runner_up_all_unique():
    arr = [10, 9, 8, 7]
    assert find_runner_up(arr) == 9


def test_runner_up_duplicates():
    arr = [5, 5, 5, 4]
    assert find_runner_up(arr) == 4
