from util import process_command

def main():
    n = int(input())
    lst = []

    for _ in range(n):
        cmd = input().split()
        result = process_command(lst, cmd)

        if result is not None:
            print(result)


if __name__ == "__main__":
    main()
