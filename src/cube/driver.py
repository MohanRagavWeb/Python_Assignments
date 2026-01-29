from src.cube.util import can_stack_blocks

def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        blocks = list(map(int, input().split()))

        result = can_stack_blocks(blocks)
        print("Yes" if result else "No")


if __name__ == "__main__":
    main()
