import numpy as np
from src.mean.util import calculate_statistics

def main():
    n, m = map(int, input().split())
    arr = np.array([input().split() for _ in range(n)], dtype=float)

    mean_vals, var_vals, std_val = calculate_statistics(arr)

    print(mean_vals)
    print(var_vals)
    print(std_val)


if __name__ == "__main__":
    main()
