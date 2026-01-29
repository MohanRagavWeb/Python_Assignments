from src.textalign.util import text_aligning

def main():
    thickness = int(input().strip())
    logo_lines = text_aligning(thickness)

    for line in logo_lines:
        print(line)


if __name__ == "__main__":
    main()
