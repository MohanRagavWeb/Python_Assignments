import numpy as np
from src.mean.util import calculate_statistics


def test_basic_case():
    arr = np.array([
        [1, 2],
        [3, 4]
    ], dtype=float)

    mean_vals, var_vals, std_val = calculate_statistics(arr)

    assert np.allclose(mean_vals, np.array([1.5, 3.5]))
    assert np.allclose(var_vals, np.array([1.0, 1.0]))
    assert round(std_val, 11) == round(np.std(arr), 11)


def test_single_row():
    arr = np.array([[5, 10, 15]], dtype=float)

    mean_vals, var_vals, std_val = calculate_statistics(arr)

    assert np.allclose(mean_vals, np.array([10.0]))
    assert np.allclose(var_vals, np.array([0.0, 0.0, 0.0]))


def test_single_column():
    arr = np.array([
        [2],
        [4],
        [6]
    ], dtype=float)

    mean_vals, var_vals, std_val = calculate_statistics(arr)

    assert np.allclose(mean_vals, np.array([2.0, 4.0, 6.0]))
    assert np.allclose(var_vals, np.array([2.66666667]))


def test_decimal_values():
    arr = np.array([
        [1.5, 2.5],
        [3.5, 4.5]
    ], dtype=float)

    mean_vals, var_vals, std_val = calculate_statistics(arr)

    assert np.allclose(mean_vals, np.array([2.0, 4.0]))
