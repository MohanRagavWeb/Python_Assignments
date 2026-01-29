import numpy as np

def calculate_statistics(arr):
    mean_vals = np.mean(arr, axis=1)
    var_vals = np.var(arr, axis=0)
    std_val = round(np.std(arr), 11)

    return mean_vals, var_vals, std_val
