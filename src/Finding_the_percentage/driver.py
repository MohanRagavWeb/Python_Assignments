from util import calculate_average

def main():
    n = int(input())
    student_marks = {}

    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()

    result = calculate_average(student_marks, query_name)

    if result is not None:
        print("{:.2f}".format(result))


if __name__ == "__main__":
    main()
