import numpy as np
from src.minmax.util import find_max_of_row_mins


def test_basic_case():
    arr = np.array([
        [2, 5, 4],
        [1, 3, 2],
        [7, 8, 9]
    ])
    assert find_max_of_row_mins(arr) == 7


def test_single_row():
    arr = np.array([[5, 6, 7]])
    assert find_max_of_row_mins(arr) == 5


def test_single_column():
    arr = np.array([
        [5],
        [3],
        [9]
    ])
    assert find_max_of_row_mins(arr) == 9


def test_negative_values():
    arr = np.array([
        [-1, -5],
        [-2, -3]
    ])
    assert find_max_of_row_mins(arr) == -3

