import numpy as np
from src.determinant.util import calculate_determinant

def main():
    n = int(input())
    matrix = np.array([input().split() for _ in range(n)], dtype=float)

    result = calculate_determinant(matrix)
    print(result)


if __name__ == "__main__":
    main()
