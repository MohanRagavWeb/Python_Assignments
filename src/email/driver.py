from src.email.util import filter_mail

def main():
    n = int(input())
    emails = [input() for _ in range(n)]

    filtered_emails = filter_mail(emails)
    print(filtered_emails)


if __name__ == "__main__":
    main()
