import numpy as np

def find_max_of_row_mins(arr):
    row_mins = np.min(arr, axis=1)
    return int(np.max(row_mins))
