from src.string_formatting.util import format_numbers

def main():
    n = int(input())
    lines = format_numbers(n)

    for line in lines:
        print(line)


if __name__ == "__main__":
    main()
