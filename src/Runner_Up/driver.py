from src.Runner_Up.util import find_runner_up

def main():
    n = int(input())
    arr = list(map(int, input().split()))

    result = find_runner_up(arr)
    print(result)


if __name__ == "__main__":
    main()
