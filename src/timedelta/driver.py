from src.timedelta.util import time_delta

def main():
    t = int(input())

    for _ in range(t):
        t1 = input()
        t2 = input()

        result = time_delta(t1, t2)
        print(result)


if __name__ == "__main__":
    main()
