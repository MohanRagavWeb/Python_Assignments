import numpy as np
from src.numpyconcept.util import apply_numpy_operations


def test_basic_values():
    floor_vals, ceil_vals, rint_vals = apply_numpy_operations(["1.1", "2.5", "3.9"])

    assert np.array_equal(floor_vals, np.array([1., 2., 3.]))
    assert np.array_equal(ceil_vals, np.array([2., 3., 4.]))
    assert np.array_equal(rint_vals, np.array([1., 2., 4.]))


def test_negative_values():
    floor_vals, ceil_vals, rint_vals = apply_numpy_operations(["-1.2", "-2.7"])

    assert np.array_equal(floor_vals, np.array([-2., -3.]))
    assert np.array_equal(ceil_vals, np.array([-1., -2.]))
    assert np.array_equal(rint_vals, np.array([-1., -3.]))


def test_whole_numbers():
    floor_vals, ceil_vals, rint_vals = apply_numpy_operations(["5.0", "6.0"])

    assert np.array_equal(floor_vals, np.array([5., 6.]))
    assert np.array_equal(ceil_vals, np.array([5., 6.]))
    assert np.array_equal(rint_vals, np.array([5., 6.]))


def test_rounding_half():
    floor_vals, ceil_vals, rint_vals = apply_numpy_operations(["2.5"])

    assert np.array_equal(rint_vals, np.array([2.])) or np.array_equal(rint_vals, np.array([3.]))
