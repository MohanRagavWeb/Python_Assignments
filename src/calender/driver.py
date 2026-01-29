from src.calender.util import get_day_name

def main():
    month, day, year = map(int, input().split())
    result = get_day_name(month, day, year)
    print(result)


if __name__ == "__main__":
    main()
