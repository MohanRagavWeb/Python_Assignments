from src.mutations.util import mutate_string

def main():
    s = input()
    i, c = input().split()

    result = mutate_string(s, int(i), c)
    print(result)


if __name__ == "__main__":
    main()
