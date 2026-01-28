def calculate_average(student_marks, query_name):
    if query_name not in student_marks:
        return None

    scores = student_marks[query_name]
    avg = sum(scores) / len(scores)
    return round(avg, 2)
