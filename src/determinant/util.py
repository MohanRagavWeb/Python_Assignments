import numpy as np

def calculate_determinant(matrix):
    det = np.linalg.det(matrix)
    return round(det, 2)
