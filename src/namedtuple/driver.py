from src.namedtuple.util import calculate_average_marks

def main():
    n = int(input())
    columns = input().split()

    records = []
    for _ in range(n):
        records.append(input().split())

    result = calculate_average_marks(n, columns, records)
    print(f"{result:.2f}")


if __name__ == "__main__":
    main()
