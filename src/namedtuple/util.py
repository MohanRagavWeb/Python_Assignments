from collections import namedtuple

def calculate_average_marks(n, columns, records):
    Student = namedtuple("Student", columns)

    total = 0
    for record in records:
        data = Student(*record)
        total += int(data.MARKS)

    return round(total / n, 2)
