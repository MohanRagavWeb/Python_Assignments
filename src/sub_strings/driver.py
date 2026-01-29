from src.sub_strings.util import merge_the_tools

def main():
    string = input()
    k = int(input())

    output = merge_the_tools(string, k)

    for line in output:
        print(line)


if __name__ == "__main__":
    main()
