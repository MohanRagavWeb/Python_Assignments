import numpy as np

np.set_printoptions(sign=' ')

def apply_numpy_operations(values):
    arr = np.array(values, dtype=float)

    floor_vals = np.floor(arr)
    ceil_vals = np.ceil(arr)
    rint_vals = np.rint(arr)

    return floor_vals, ceil_vals, rint_vals
