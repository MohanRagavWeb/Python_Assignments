from src.wordorder.util import count_words

def main():
    n = int(input())
    words = [input() for _ in range(n)]

    unique_count, counts = count_words(words)

    print(unique_count)
    print(*counts)


if __name__ == "__main__":
    main()
