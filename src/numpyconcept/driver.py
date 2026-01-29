from src.numpyconcept.util import apply_numpy_operations

def main():
    values = input().split()

    floor_vals, ceil_vals, rint_vals = apply_numpy_operations(values)

    print(floor_vals)
    print(ceil_vals)
    print(rint_vals)


if __name__ == "__main__":
    main()
