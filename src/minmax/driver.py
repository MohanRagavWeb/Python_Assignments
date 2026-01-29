import numpy as np
from src.minmax.util import find_max_of_row_mins

def main():
    n, m = map(int, input().split())
    arr = np.array([input().split() for _ in range(n)], dtype=int)

    result = find_max_of_row_mins(arr)
    print(result)


if __name__ == "__main__":
    main()
