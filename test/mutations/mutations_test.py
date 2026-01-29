from src.mutations.util import mutate_string


def test_mutate_basic():
    assert mutate_string("abracadabra", 5, "k") == "abrackdabra"


def test_mutate_first_char():
    assert mutate_string("hello", 0, "y") == "yello"


def test_mutate_last_char():
    assert mutate_string("world", 4, "!") == "worl!"


def test_mutate_middle():
    assert mutate_string("python", 3, "X") == "pytXon"
