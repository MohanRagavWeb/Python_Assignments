from src.lists.util import process_command



def test_append():
    lst = []
    process_command(lst, ["append", "5"])
    assert lst == [5]


def test_insert():
    lst = [1, 2]
    process_command(lst, ["insert", "1", "10"])
    assert lst == [1, 10, 2]


def test_remove():
    lst = [1, 2, 3]
    process_command(lst, ["remove", "2"])
    assert lst == [1, 3]


def test_sort():
    lst = [3, 1, 2]
    process_command(lst, ["sort"])
    assert lst == [1, 2, 3]


def test_reverse():
    lst = [1, 2, 3]
    process_command(lst, ["reverse"])
    assert lst == [3, 2, 1]


def test_pop():
    lst = [1, 2, 3]
    process_command(lst, ["pop"])
    assert lst == [1, 2]


def test_print():
    lst = [1, 2]
    result = process_command(lst, ["print"])
    assert result == [1, 2]
