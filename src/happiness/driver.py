from src.happiness.util import calculate_happiness

def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))

    result = calculate_happiness(arr, A, B)
    print(result)


if __name__ == "__main__":
    main()
