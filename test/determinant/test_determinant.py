import numpy as np
from src.determinant.util import calculate_determinant


def test_2x2_matrix():
    matrix = np.array([
        [1, 2],
        [3, 4]
    ], dtype=float)
    assert calculate_determinant(matrix) == -2.0


def test_identity_matrix():
    matrix = np.array([
        [1, 0],
        [0, 1]
    ], dtype=float)
    assert calculate_determinant(matrix) == 1.0


def test_3x3_matrix():
    matrix = np.array([
        [6, 1, 1],
        [4, -2, 5],
        [2, 8, 7]
    ], dtype=float)
    assert calculate_determinant(matrix) == -306.0


def test_zero_determinant():
    matrix = np.array([
        [2, 4],
        [1, 2]
    ], dtype=float)
    assert calculate_determinant(matrix) == 0.0
